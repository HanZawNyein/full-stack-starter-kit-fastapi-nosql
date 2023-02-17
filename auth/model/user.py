from pydantic import EmailStr
from beanie import Document


class User(Document):
    email: EmailStr
    password: str

    class Settings:
        name = "users"

    class Config:
        schema_extra = {
            "example": {
                "email": "hanzaw@gmail.com",
                "password": "hanzaw@gmail.com",
            }
        }
