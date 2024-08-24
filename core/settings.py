import os

from pydantic import Field
from pydantic_settings import BaseSettings, SettingsConfigDict

env = os.environ.get("ENV", "")


class Settings(BaseSettings):
    env: str = Field(alias='ENV')
    service_name: str = Field(alias='SERVICE_NAME')
    kis_base_url: str = Field(alias='KIS_BASE_URL')

    model_config = SettingsConfigDict(
        env_file_encoding='utf-8',
        env_file=('.env', f'.env.{env}'),
        extra='ignore'
    )


settings = Settings(_env_file_encoding='utf-8')
