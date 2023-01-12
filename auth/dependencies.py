from fastapi import Depends
from fastapi.security import OAuth2PasswordBearer

from .schemas import UserForDB


def get_current_user(token: str = Depends(OAuth2PasswordBearer)) -> UserForDB | None:
    """Зависимость, возвращающая схему текущего пользователя по jwt-токену"""
    pass