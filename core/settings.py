import logging
import os

from pydantic import Field, PostgresDsn, computed_field
from pydantic_core import MultiHostUrl
from pydantic_settings import BaseSettings, SettingsConfigDict

logger = logging.getLogger('uvicorn.info')
env = os.environ.get("ENV", "")

logger.info(f'Running in {env} environment')


class Settings(BaseSettings):
    env: str = Field(alias='ENV')
    service_name: str = Field(alias='SERVICE_NAME')
    kis_base_url: str = Field(alias='KIS_BASE_URL')

    model_config = SettingsConfigDict(
        env_file_encoding='utf-8',
        extra='ignore'
    )

    DB_HOST: str
    DB_PORT: int = 5432
    DB_NAME: str = ""
    DB_USER: str
    DB_PASS: str = ""

    @computed_field
    @property
    def SQLALCHEMY_DATABASE_URI(self) -> PostgresDsn:
        return MultiHostUrl.build(
            scheme="postgresql+psycopg2",
            host=self.DB_HOST,
            port=self.DB_PORT,
            path=self.DB_NAME,
            username=self.DB_USER,
            password=self.DB_PASS,
        )


settings = Settings(_env_file=('.env.local', f'.env.local.{env}'), _env_file_encoding='utf-8')
