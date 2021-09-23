import os
import pathlib

ENVIRONMENT = os.getenv("ENVIRONMENT")
if ENVIRONMENT is None:
    from dotenv import load_dotenv

    load_dotenv(dotenv_path=f"{os.getcwd()}/.env")

PREFIX = os.getenv("PREFIX", "!")

TOKEN = os.getenv("TOKEN")

EXTENSIONS = pathlib.Path("bot/exts/")
