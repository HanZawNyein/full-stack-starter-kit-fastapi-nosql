from pydantic import BaseModel


class TokenResponse(BaseModel):
    access_token: str
    token_type: str

    class Config:
        schema_extra = {
            "example": {
                "access_token": "****",
                "token_type": "Bearer"
            }
        }
