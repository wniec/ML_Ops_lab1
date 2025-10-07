import os

import pytest
from pydantic_core._pydantic_core import ValidationError

from settings import Settings
from dotenv import load_dotenv


@pytest.fixture()
def export_envs() -> None:
    dotenv_file = ".env.test"
    load_dotenv(dotenv_file)


def test_settings_pass(export_envs):
    settings = Settings(
        ENVIRONMENT=os.environ.get("ENVIRONMENT"),
        APP_NAME=os.environ.get("APP_NAME"),
        SECRET="SECRET",
    )
    assert settings.ENVIRONMENT == os.environ.get("ENVIRONMENT")
    assert settings.APP_NAME == os.environ.get("APP_NAME")
    assert settings.SECRET == "SECRET"


def test_settings_fail(export_envs):
    with pytest.raises(ValidationError):
        Settings(
            ENVIRONMENT="anomalia",
            APP_NAME=os.environ.get("APP_NAME"),
            SECRET=os.environ.get("key"),
        )
