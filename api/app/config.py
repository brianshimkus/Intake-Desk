from functools import lru_cache
from typing import Literal

from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    app_name: str = "Intake Desk API"
    environment: Literal["development", "test", "production"] = "development"
    database_url: str = "sqlite:///./intake_desk.db"
    web_origin: str = "http://localhost:3000"

    extraction_mode: Literal["fake", "openai"] = "fake"
    openai_api_key: str = ""
    openai_model: str = "gpt-6-astra"

    # In production this stays true: only server-owned fictional samples are accepted.
    demo_mode: bool = True
    max_source_characters: int = 6_000

    model_config = SettingsConfigDict(env_file=".env", extra="ignore")


@lru_cache
def get_settings() -> Settings:
    return Settings()
