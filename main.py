import os
import argparse

import yaml
from dotenv import load_dotenv
from settings import Settings


def export_envs(environment: str = "dev") -> None:
    dotenv_file = f".env.{environment}"
    load_dotenv(dotenv_file)


if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description="Load environment variables from specified.env file."
    )
    parser.add_argument(
        "--environment",
        type=str,
        default="dev",
        help="The environment to load (dev, test, prod)",
    )
    args = parser.parse_args()
    export_envs(args.environment)
    with open("secrets.yaml", "r") as file:
        yaml_content = yaml.safe_load(file)
    for key, val in yaml_content.items():
        os.environ[key] = val
    settings = Settings(
        ENVIRONMENT=os.environ.get("ENVIRONMENT"),
        APP_NAME=os.environ.get("APP_NAME"),
        SECRET=os.environ.get("key"),
    )

    print("APP_NAME: ", settings.APP_NAME)
    print("ENVIRONMENT: ", settings.ENVIRONMENT)
    print("SECRET: ", settings.SECRET)
