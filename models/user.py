from sqlalchemy import Column, String, DateTime, Date, Enum
from sqlalchemy.orm import relationship
import enum
from .base import Base


class Gender(enum.Enum):
    MALE = "Male"
    FEMALE = "Female"


class AccountStatus(enum.Enum):
    ACTIVE = "active"
    INACTIVE = "inactive"


class User(Base):
    __tablename__ = 'users'

    username = Column(String, unique=True, nullable=False)
    preferred_name = Column(String, nullable=False)
    gender = Column(Enum(Gender), nullable=False)
    date_of_birth = Column(Date, nullable=False)
    last_active = Column(DateTime)
    account_status = Column(Enum(AccountStatus), default=AccountStatus.INACTIVE, nullable=False)
    password_hash = Column(String, nullable=False)

    emotion_logs = relationship("EmotionLog", back_populates="user")

