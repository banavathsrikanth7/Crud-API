from fastapi import APIRouter
from app.services.db_queries import get_data

router = APIRouter(prefix="/videos", tags=["Videos"])


@router.get("/db_queries")
def db_queries():

    result = get_data(
        columns=["Reels", "Channel"],
        limit=100
    )

    return result
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