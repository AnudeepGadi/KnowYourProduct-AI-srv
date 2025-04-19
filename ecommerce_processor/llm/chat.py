from typing import Dict, Generator, List
from ecommerce_processor.factories.llm_factory import LLMFactory

def ask_llm(messages:List[Dict]):
    """
    Function to query the LLM with a list of messages.
    """
    llm = LLMFactory.create_llm("llama4")
    response = llm.generate_response(messages)
    return response

def ask_llm_stream(messages:List[Dict]) -> Generator[str, None, None]:
    """
    Function to query the LLM with a list of messages and return a generator for streaming responses.
    """
    llm = LLMFactory.create_llm("llama4")
    for chunk in llm.generate_streaming_response(messages):
        yield chunk