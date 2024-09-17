from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, DateTime
from datetime import datetime


class BaseModel(object):
    """Base class for all model"""
    id = Column(Integer, primary_key=True)
    created_at = Column(DateTime, default=datetime.now)

    # updated_at = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)

    def __repr__(self):
        return f"<{self.__class__.__name__}(id={self.id})>"


Base = declarative_base(cls=BaseModel)
