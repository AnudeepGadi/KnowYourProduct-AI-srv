from pydantic_settings import BaseSettings
from pydantic import Field

class Settings(BaseSettings):
    APP_NAME: str = Field(..., env="APP_NAME")
    APP_VERSION: str = Field(..., env="APP_VERSION")
    FIREWORKS_API_KEY: str = Field(..., env="FIREWORKS_API_KEY")
    FIREWORKS_API_BASE: str = Field(..., env="FIREWORKS_API_BASE")
    FIREWORKS_LLAMA_MODEL_NAME: str = Field(..., env="FIREWORKS_LLAMA_MODEL_NAME")
    MAX_TOKENS: int = Field(2000, env="MAX_TOKENS")
    TEMPERATURE: float = Field(0.1, env="TEMPERATURE")

    class Config:
        env_file = ".env"