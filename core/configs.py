from pydantic.v1 import BaseSettings
from sqlalchemy.orm import declarative_base

class Settings(BaseSettings):
    API_V1_STR: str = "/api/v1" 
    DB_URL: str = "mysql+aiomysql://root:root@127.0.0.1:3306/office_characters" 
    DBBaseModel = declarative_base() 

class Config:
    case_sensitive = False  
    env_file = "env" 

settings = Settings()
