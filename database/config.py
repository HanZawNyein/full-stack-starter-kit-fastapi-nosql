from pydantic import BaseSettings
from typing import Optional
from motor.motor_asyncio import AsyncIOMotorClient
from beanie import init_beanie

# auth
from auth.model import User
from post.model import Post

class Settings(BaseSettings):
    DATABASE_URL: Optional[str] = None
    DEFAULT_DATABASE: Optional[str] = None
    SECRET_KEY:Optional[str]=None

    async def initialize_database(self, default_databse):
        client = AsyncIOMotorClient(self.DATABASE_URL)
        await init_beanie(database=client.get_default_database(default_databse),
                          document_models=[User,Post]
                          )

    class Config:
        env_file = ".env"


settings = Settings()
