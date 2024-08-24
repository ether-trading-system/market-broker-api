import os

from pydantic import Field
from pydantic_settings import BaseSettings, SettingsConfigDict

env = os.environ.get("ENV", "")


class Settings(BaseSettings):
    service_name: str = Field(alias='SERVICE_NAME')
    kis_real_base_url: str = Field(alias='KIS_REAL_BASE_URL')
    kis_real_app_key: str = Field(alias='KIS_REAL_APP_KEY')
    kis_real_app_secret: str = Field(alias='KIS_REAL_APP_SECRET')
    kis_base_url: str = Field(alias='KIS_BASE_URL')

    model_config = SettingsConfigDict(
        env_file_encoding='utf-8',
        env_file=('.env', f'.env.{env}'),
        extra='ignore'
    )


settings = Settings(_env_file_encoding='utf-8')
