# settings.py
from pydantic_settings import BaseSettings
from pydantic import validator


class Settings(BaseSettings):
    ENVIRONMENT: str
    APP_NAME: str
    SECRET: str

    @validator("ENVIRONMENT")
    def validate_environment(cls, value):
        if value not in ("dev", "test", "prod"):
            raise ValueError("Invalid ENVIROMENT value: {value}")
        # prepare validator that will check whether the value of ENVIRONMENT is in (dev, test, prod)
        return value
