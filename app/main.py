from fastapi import FastAPI
from app.routers import videos
from dotenv import load_dotenv
load_dotenv()
app = FastAPI()


app.include_router(videos.router)