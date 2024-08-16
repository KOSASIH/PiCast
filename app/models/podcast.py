from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class Podcast(Base):
    __tablename__ = 'podcasts'
    id = Column(Integer, primary_key=True)
    title = Column(String)
    description = Column(String)
    audio_file = Column(String)
    created_at = Column(DateTime, default=datetime.utcnow)
    updated_at = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)
