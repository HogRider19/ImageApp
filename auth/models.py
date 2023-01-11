from db.database import Base
from sqlalchemy import Column, Integer, String, DATETIME, Boolean
import datetime


class Role(Base):
    """Модель ролей пользователей"""
    pass

class User(Base):
    """Модель пользователя"""

    __tablename__ = 'users'

    username = Column(String, nullable=False)
    email = Column(String, nullable=False)
    hashed_password = Column(String, nullable=False)
    registed_at = Column(DATETIME, default=datetime.datetime.utcnow)
    is_active = Column(Boolean, default=True, nullable=False)

