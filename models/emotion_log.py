from sqlalchemy import Column, Integer, ForeignKey, Float
from sqlalchemy.orm import relationship
from .base import Base


class EmotionLog(Base):
    __tablename__ = 'emotion_logs'

    neutral = Column(Float, nullable=False)
    happiness = Column(Float, nullable=False)
    sadness = Column(Float, nullable=False)
    anger = Column(Float, nullable=False)
    fear = Column(Float, nullable=False)
    surprise = Column(Float, nullable=False)
    disgust = Column(Float, nullable=False)
    contempt = Column(Float, nullable=False)
    user_id = Column(Integer, ForeignKey('users.id'))

    user = relationship("User", back_populates="emotion_logs")
