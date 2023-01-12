from passlib.hash import bcrypt
from sqlalchemy.orm import Session

from .models import User
from .schemas import UserForDB


def get_hashed_password(password: str) -> str:
    """Фнкция, хешируюая пароль"""
    return bcrypt.hash(password)

def verify_password(raw_password: str, hashed_password: str) -> bool:
    """Проверяет соотвентсвие пароля и хэшированного-пароля"""
    return bcrypt.verify(raw_password, hashed_password)

def decode_token(token: str) -> int | None:
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
            registed_at=user_db.registed_at,
            is_superuser=user_db.is_superuser,
            role_id=user_db.role_id)
         

def get_user(token: str) -> UserForDB | None:
    """Возвращающая схему пользователя по jwt-токену"""
    pass