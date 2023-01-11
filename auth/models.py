from db.database import Base
from sqlalchemy import Column, Integer, String, DATETIME, Boolean, ForeignKey
import datetime


class Role(Base):
    """Модель ролей пользователей"""
    
    __tablename__ = 'roles'

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String, nullable=False)

    

class User(Base):
    """Модель пользователя"""

    __tablename__ = 'users'

    id = Column(Integer, primary_key=True, autoincrement=True)
    username = Column(String, nullable=False)
    email = Column(String, nullable=False)
    hashed_password = Column(String, nullable=False)
    registed_at = Column(DATETIME, default=datetime.datetime.utcnow)
    is_active = Column(Boolean, default=True, nullable=False)
    is_superuser = Column(Boolean, default=False, nullable=False)
    role_id = Column(Integer, ForeignKey('roles.id'))
