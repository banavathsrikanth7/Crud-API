from fastapi import FastAPI
from app.routers import videos
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Create FastAPI app
app = FastAPI()

# Include router
app.include_router(videos.router)


# Test endpoint to check if API is working
@app.get("/")
def root():
    return {"message": "Frammer Analytics API is working 🚀"}