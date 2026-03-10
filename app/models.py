from sqlalchemy import Column, Integer, String, ForeignKey, Boolean, Time, TIMESTAMP
from .database import Base


class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    username = Column(String)


class Team(Base):
    __tablename__ = "teams"

    id = Column(Integer, primary_key=True)
    name = Column(String)


class Channel(Base):
    __tablename__ = "channels"

    id = Column(Integer, primary_key=True)
    name = Column(String)


class Language(Base):
    __tablename__ = "languages"

    id = Column(Integer, primary_key=True)
    code = Column(String)


class InputType(Base):
    __tablename__ = "input_types"

    id = Column(Integer, primary_key=True)
    name = Column(String)


class OutputType(Base):
    __tablename__ = "output_types"

    id = Column(Integer, primary_key=True)
    name = Column(String)


class Platform(Base):
    __tablename__ = "platforms"

    id = Column(Integer, primary_key=True)
    name = Column(String)


class Video(Base):
    __tablename__ = "videos"

    video_id = Column(String, primary_key=True)
    headline = Column(String)
    source_url = Column(String)

    channel_id = Column(Integer, ForeignKey("channels.id"))
    uploaded_by_user_id = Column(Integer, ForeignKey("users.id"))
    team_id = Column(Integer, ForeignKey("teams.id"))
    input_type_id = Column(Integer, ForeignKey("input_types.id"))
    language_id = Column(Integer, ForeignKey("languages.id"))

    uploaded_duration = Column(Time)
    uploaded_at = Column(TIMESTAMP)


class VideoCreation(Base):
    __tablename__ = "video_creations"

    creation_id = Column(Integer, primary_key=True)

    video_id = Column(String, ForeignKey("videos.video_id"))
    output_type_id = Column(Integer, ForeignKey("output_types.id"))

    created_duration = Column(Time)
    created_at = Column(TIMESTAMP)


class VideoPublication(Base):
    __tablename__ = "video_publications"

    publish_id = Column(Integer, primary_key=True)

    video_id = Column(String, ForeignKey("videos.video_id"))
    platform_id = Column(Integer, ForeignKey("platforms.id"))

    published_url = Column(String)
    is_published = Column(Boolean)
    published_duration = Column(Time)
    published_at = Column(TIMESTAMP)