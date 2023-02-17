import uvicorn
from fastapi import FastAPI

# routes
from .route import router

app = FastAPI()

app.include_router(router)
