from functools import lru_cache
from typing import Any, Dict, Optional

from pydantic import BaseSettings, PostgresDsn, conint, validator


class AppSettings(BaseSettings):
    PROJECT_NAME: str = 'app'

    DB_URI: Optional[PostgresDsn] = "postgresql+psycopg2://postgres:postgres@db:5432"


@lru_cache()
def get_settings() -> AppSettings:
    return AppSettings()
