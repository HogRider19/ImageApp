from db.database import Base
from auth.models import User
from sqlalchemy import Integer, String, ForeignKey, Column, TIMESTAMP
from sqlalchemy.orm import relationship
import datetime


class Image(Base):
    """Модель изображения"""
    __tablename__ = 'images'

    id = Column(Integer, primary_key=True, autoincrement=True)
    title = Column(String(100), nullable=False)
    description = Column(String(500), nullable=True)
    path = Column(String, nullable=False, unique=True)
    user_id = Column(Integer, ForeignKey('users.id'))
    liks = Column(Integer, default=0, nullable=False)
    created_at = Column(TIMESTAMP, default=datetime.datetime.utcnow)
