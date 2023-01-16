import datetime

from pydantic import BaseModel, Field


class Role(BaseModel):
    id: int
    name: str

class BaseUser(BaseModel):
    username: str = Field(min_length=4, max_length=50)
    registed_at: datetime.datetime
    is_active: bool = True
    is_superuser: bool = False
    role_id: int | None

class UserIn(BaseUser):
    password: str = Field(min_length=8, max_length=30)
    email: str = Field(max_length=100)

class UserForDB(BaseUser):
    id: int
    email: str = Field(max_length=100)
    hashed_password: str

    class Config:
        orm_mode = True

class UserOut(BaseUser):
    pass

class UserCreate(UserIn):
    pass

class Token(BaseModel):
    access_token: str
    token_type: str

class TokenData(BaseModel):
    username: str | None = None

