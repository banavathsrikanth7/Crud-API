from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.database import SessionLocal
from app.models import Video

router = APIRouter(prefix="/videos", tags=["Videos"])

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@router.get("/")
def get_videos(db: Session = Depends(get_db)):
    return db.query(Video).all()


@router.post("/")
def create_video(video_id: str, headline: str, db: Session = Depends(get_db)):
    video = Video(video_id=video_id, headline=headline)
    db.add(video)
    db.commit()
    db.refresh(video)
    return video


@router.delete("/{video_id}")
def delete_video(video_id: str, db: Session = Depends(get_db)):
    video = db.query(Video).filter(Video.video_id == video_id).first()
    db.delete(video)
    db.commit()
    return {"message": "video deleted"}