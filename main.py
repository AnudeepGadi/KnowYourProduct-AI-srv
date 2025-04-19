from fastapi import FastAPI, WebSocket, WebSocketDisconnect
import json
from uuid import uuid4
from ecommerce_processor.factories.processor_factory import EcommerceProcessorFactory
from ecommerce_processor.llm.chat import ask_llm
from ecommerce_processor.models.chat_session import ChatSession
from config import Settings

settings = Settings()
app = FastAPI(title=settings.APP_NAME, version=settings.APP_VERSION)

@app.websocket("/chat")  # No path/query params needed
async def websocket_endpoint(websocket: WebSocket):
    await websocket.accept()
    session_id = None
    source = None
    
    try:
        # Phase 1: Initialization
        init_msg = await websocket.receive_json()
        if init_msg.get("type") != "initialize":
            await websocket.send_json({"error": "First message must be initialization"})
            await websocket.close()
            return
            
        source = init_msg["source"]
        session_id = str(uuid4())
        chat_session = ChatSession(session_id=session_id, source=source)


        await websocket.send_json({
            "type": "initialized",
            **ChatSession.to_user_dict(chat_session)
        })

        # Phase 2: HTML Transfer
        html_msg = await websocket.receive_json()
        if html_msg.get("type") != "html_data":
            await websocket.send_json({"error": "Expected HTML data"})
            await websocket.close()
            return
        
        chat_session.html_content = html_msg["html_content"]
        builder = EcommerceProcessorFactory.create_processor(chat_session.source)
        chat_session.prompt = (
            builder.parse_html(chat_session.html_content)
                .generate_prompt(r"ecommerce_processor/prompt_templates/product_prompt.md")
                .build()
        )
        chat_session.messages = [{"role": "system", "content": chat_session.prompt}]
        await websocket.send_json({"type": "html_ack", "status": "success"})

        # Phase 3: Querying Phase
        while True:
            query_msg = await websocket.receive_json()
            if query_msg.get("type") == "query":
                question = query_msg["question"]
                chat_session.messages.append({"role": "user", "content": question})
                llm_response = ask_llm(chat_session.messages)
                chat_session.messages.append({"role": "assistant", "content": llm_response})
                await websocket.send_json({
                    "type": "query_response",
                    "response": llm_response
                })
                
    except WebSocketDisconnect:
        if session_id:
            del chat_session
            print(f"Cleaning up session: {session_id}")
            