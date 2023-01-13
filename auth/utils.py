from datetime import datetime, timedelta

from jose import jwt
from passlib.hash import bcrypt
from sqlalchemy.orm import Session

from config.config import ALGORITHM_JWT, SECRET_JWT, TOKEN_LIFETIME_MINUTES

from .models import User
from .schemas import UserForDB


def get_hashed_password(password: str) -> str:
    """Фнкция, хешируюая пароль"""
    return bcrypt.hash(password)

def verify_password(raw_password: str, hashed_password: str) -> bool:
    """Проверяет соотвентсвие пароля и хэшированного-пароля"""
    return bcrypt.verify(raw_password, hashed_password)

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

def decode_token(token: str) -> dict | None:
    """Расшифровывает jwt-токен и возвращает его  payload"""
    return jwt.decode(token, key=SECRET_JWT, algorithms=[ALGORITHM_JWT])

def create_access_token(data: dict, expires_delta: timedelta | None = None) -> str:
    """Создает jwt-токен с телом data"""
    to_encode = data.copy()
    if expires_delta:
        expire = datetime.utcnow() + expires_delta
    else:
        expire = datetime.utcnow() + timedelta(minutes=TOKEN_LIFETIME_MINUTES)
    to_encode.update({"exp": expire})
    encoded_jwt = jwt.encode(to_encode, SECRET_JWT, algorithm=ALGORITHM_JWT)
    return encoded_jwt