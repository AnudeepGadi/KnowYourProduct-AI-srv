from typing import Dict, List
from ecommerce_processor.factories.llm_factory import LLMFactory

def ask_llm(messages:List[Dict]):
    """
    Function to query the LLM with a list of messages.
    """
    llm = LLMFactory.create_llm("llama4")
    response = llm.generate_response(messages)
    return response