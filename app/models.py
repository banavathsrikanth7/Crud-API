from sqlalchemy import Column, String
from .database import Base

class Video(Base):
    __tablename__ = "videos"

    video_id = Column(String, primary_key=True)
    headline = Column(String)
    source_url = Column(String)