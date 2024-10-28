import os
import logging

from pydantic import Field
from pydantic_settings import BaseSettings, SettingsConfigDict

logger = logging.getLogger('uvicorn.info')
env = os.environ.get("ENV", "")

logger.info(f'Running in {env} environment')


class Settings(BaseSettings):
    env: str = Field(alias='ENV')
    service_name: str = Field(alias='SERVICE_NAME')
    kis_base_url: str = Field(alias='KIS_BASE_URL')
    kis_real_app_key: str = Field(alias='KIS_REAL_APP_KEY')
    kis_real_app_secret: str = Field(alias='KIS_REAL_APP_SECRET')

    model_config = SettingsConfigDict(
        env_file_encoding='utf-8',
        extra='ignore'
    )


settings = Settings(_env_file=('.env', f'.env.{env}'), _env_file_encoding='utf-8')
