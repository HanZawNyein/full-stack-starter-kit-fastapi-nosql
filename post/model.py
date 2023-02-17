from beanie import Document
from typing import Optional


class Post(Document):
    title: str
    description: str
    creator: Optional[str]

    class Settings:
        name = "posts"

    class Config:
        schema_extra = {
            "example": {
                "_id": "63eed4d838c57c5722c80650",
                "title": "What is FastAPI ?",
                "description": "hanzaw@gmail.com",
                "creator": "hanzaw@gmail.com"
            }
        }
