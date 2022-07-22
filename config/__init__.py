from pydantic import BaseSettings
from dotenv import load_dotenv
import os

load_dotenv()

debug = os.getenv("DEBUG_MODE")
db_url = os.getenv("DB_URL")
db_name = os.getenv("DB_NAME")

class CommonSetts(BaseSettings):
    APP_NAME: str = "FARM Stack Template"
    DEBUG_MODE: bool = debug


class ServerSetts(BaseSettings):
    HOST: str = "127.0.0.1"
    PORT: int = 8080


class DBSetts(BaseSettings): # infos about MongoDB
    DB_URL: str = db_url
    DB_NAME: str = db_name

class GeneralSetts(CommonSetts, ServerSetts, DBSetts):
    pass


settings = GeneralSetts()
