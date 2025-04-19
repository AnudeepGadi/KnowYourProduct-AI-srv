from ecommerce_processor.llm.models import AbstractLLM


class LLMFactory:
    @staticmethod
    def create_llm(model_name: str) -> AbstractLLM:
        model_dict = {}
        if model_name not in model_dict:
            if model_name == "llama4":
                from ecommerce_processor.llm.models import create_llama4_client
                model_dict[model_name] = create_llama4_client()
            else:       
                raise ValueError(f"Unsupported LLM source: {model_name}")
        return model_dict[model_name]