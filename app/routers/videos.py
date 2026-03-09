from fastapi import APIRouter
from sqlalchemy.orm import Session
from app.database import SessionLocal
from app.models import Video

router = APIRouter(prefix="/videos")

@router.post("/")
def create_video(video_id: str, headline: str):

    db = SessionLocal()

    video = Video(video_id=video_id, headline=headline)

    db.add(video)
    db.commit()

    return video


@router.get("/")
def get_videos():

    db = SessionLocal()

    return db.query(Video).all()


@router.delete("/{video_id}")
def delete_video(video_id: str):

    db = SessionLocal()

    video = db.query(Video).filter(Video.video_id == video_id).first()

    db.delete(video)

    db.commit()

    return {"message": "deleted"}