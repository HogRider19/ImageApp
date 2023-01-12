from datetime import datetime, timedelta

from fastapi import Depends, HTTPException, status
from fastapi.security import OAuth2PasswordBearer
from jose import JWTError, jwt

from config.config import ALGORITHM_JWT, SECRET_JWT, TOKEN_LIFETIME_MINUTES

from .schemas import UserForDB, TokenData

from .utils import get_user_by_username, decode_token

from db.database import get_db

from sqlalchemy.orm import Session


oauth2_scheme = OAuth2PasswordBearer(tokenUrl='/auth/login')

async def get_current_user(
    token: str = Depends(OAuth2PasswordBearer),
    db: Session = Depends(get_db)) -> UserForDB | None:
    """Зависимость, возвращающая схему текущего пользователя по jwt-токену"""
    credentials_exception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Could not validate credentials",
        headers={"WWW-Authenticate": "Bearer"})
    try:
        payload = decode_token(token)
        username: str = payload.get('sub')
        if username is None:
            raise credentials_exception
        token_data = TokenData(username=username)
    except JWTError:
        raise credentials_exception
    
    user = get_user_by_username(token_data.username, db_session=db)

    if user is None:
        raise credentials_exception

    return user

async def get_curren_active_user(user: UserForDB = Depends(get_current_user)):
    """
    Зависимость, возвращающая схему текущего активного пользователя по jwt-токену
    """
    if not user.is_active:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail='Inactive user'
        )
    return user


