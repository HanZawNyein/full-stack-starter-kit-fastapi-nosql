import uvicorn
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

# database
from database import settings

# sub apps
from auth.main import app as auth_app
from post.main import app as post_app


# origins
origins = ["*"]

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"]
)


@app.on_event("startup")
async def init_db():
    await settings.initialize_database(default_databse=settings.DEFAULT_DATABASE)

# sub apps
app.mount("/auth", auth_app)
app.mount("/post", post_app)

if __name__ == "__main__":
    uvicorn.run('main:app', host="0.0.0.0", port=8080, reload=True)
