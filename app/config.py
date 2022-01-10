from os import access
from pydantic import BaseSettings

class Settings(BaseSettings):
    access_token_expire_minutes: int
    database_hostname: str
    database_username: str
    database_password: str
    database_name: str
    database_port: str
    secret_key: str
    algorithm: str

    class Config:
        env_file = '.env'


settings = Settings()