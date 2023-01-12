from fastapi import Depends
from fastapi.security import OAuth2PasswordBearer
from passlib.hash import bcrypt

from .schemas import UserForDB, UserIn, Role
from .models import User

from sqlalchemy.orm import Session



def get_hashed_password(password: str) -> str:
    """Фнкция, хешируюая пароль"""
    return bcrypt.hash(password)

def verify_password(raw_password: str, hashed_password: str) -> bool:
    """Проверяет соотвентсвие пароля и хэшированного-пароля"""
    return bcrypt.verify(raw_password, hashed_password)

async def decode_token(token: str) -> int | None:
    """Расшифровывает jwt-токен и возвращает id пользователя"""
    pass

def get_user_by_username(username: str, db_session: Session) -> UserForDB | None:
    """Возвращает пользователя с переданным именем"""
    user_db = db_session.query(User).filter(User.username == username).first()
    if user_db:
        return UserForDB(
            username = user_db.username,
            email=user_db.email,
            hashed_password=user_db.hashed_password,
            registed_at=user_db.registed_atm,
            is_superuser=user_db.is_superuser,
            role_id=user_db.role_id)
         

async def get_user(token: str) -> UserForDB | None:
    """Возвращающая схему пользователя по jwt-токену"""
    pass

async def get_current_user(token: str = Depends(OAuth2PasswordBearer)) -> UserForDB | None:
    """Зависимость, возвращающая схему текущего пользователя по jwt-токену"""
    pass