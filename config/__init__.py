from pydantic import BaseSettings

class CommonSetts(BaseSettings):
    APP_NAME: str = "FARM Stack Template"
    DEBUG_MODE: bool = False


class ServerSetts(BaseSettings):
    HOST: str = "127.0.0.1"
    PORT: int = 8888


class DBSetts(BaseSettings):
    DB_URL: str
    DB_NAME: str

class GeneralSetts(CommonSetts, ServerSetts, DBSetts):
    pass


settings = GeneralSetts()
