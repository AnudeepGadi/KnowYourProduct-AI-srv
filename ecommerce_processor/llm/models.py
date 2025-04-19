from abc import ABC, abstractmethod
from typing import Dict, List
from config import Settings
from openai import OpenAI
from typing import Dict, List, Generator
import json


settings = Settings()

class AbstractLLM(ABC):
    def __init__(self):
        super().__init__()
        self.client = None
        self.temperature = settings.TEMPERATURE
        self.max_tokens = settings.MAX_TOKENS
    
    @abstractmethod
    def init_model(self):
        """
        Initialize the model.
        """
        pass

    @abstractmethod
    def generate_response(self, prompt: str) -> str:
        """
        Generate a response from the model based on the given prompt.
        """
        pass


def create_llama4_client() -> OpenAI:
    """
    Create an Llama4 client instance.
    """
    class LLama4LLM(AbstractLLM):
        def __init__(self, model_name: str):
            super().__init__()
            self.init_model(model_name)
            
        def init_model(self,model_name: str):
            """
            Initialize the Llama4 model.
            """
            self.model_name = model_name
            self.client = OpenAI(
                api_key=settings.FIREWORKS_API_KEY,
                base_url=settings.FIREWORKS_API_BASE,
            )
        
        def generate_response(self, messages:List[Dict]) -> str:
            response = self.client.chat.completions.create(
                model=self.model_name,
                temperature=self.temperature,
                max_tokens=self.max_tokens,
                messages=messages,
                stream=False
            )
            return response.choices[0].message.content

        def generate_streaming_response(self, messages: List[Dict]) -> Generator[str, None, None]:
            stream = self.client.chat.completions.create(
                     model=self.model_name,
                    temperature=self.temperature,
                    max_tokens=self.max_tokens,
                    messages=messages,
                    stream=True
            )

            for chunk in stream:
                if chunk.choices[0].delta.content is not None:
                    yield chunk.choices[0].delta.content
                
    return LLama4LLM(model_name=settings.FIREWORKS_LLAMA_MODEL_NAME)
            
