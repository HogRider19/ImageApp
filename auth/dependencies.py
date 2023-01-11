from fastapi import Depends
from fastapi.security import OAuth2PasswordBearer

from .schemas import UserForDB, UserIn


class PasswordHasher():
    """Класс-зависимость хеширующий пароль"""
    
    def __init__(self, secret_key: str) -> None:
        self._secret_key = secret_key

    def __call__(self, password) -> str:
        pass


async def decode_token(token: str) -> int | None:
    """Расшифровывает jwt-токен и возвращает id пользователя"""
    pass

async def get_user(token: str) -> UserForDB | None:
    """Возвращающая схему пользователя по jwt-токену"""
    pass

async def get_current_user(token: str = Depends(OAuth2PasswordBearer)) -> UserForDB | None:
    """Зависимость, возвращающая схему текущего пользователя по jwt-токену"""
    pass