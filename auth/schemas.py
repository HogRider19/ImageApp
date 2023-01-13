from pydantic import BaseModel, Field
import datetime


class Role(BaseModel):
    id: int
    name: str

class BaseUser(BaseModel):
    username: str = Field(min_length=4, max_length=50)
    email: str = Field(max_length=100)
    registed_at: datetime.datetime
    is_active: bool = True
    is_superuser: bool = False
    role_id: int | None

class UserIn(BaseUser):
    password: str = Field(min_length=8, max_length=30)

class UserCreate(UserIn):
    password_repeat: str = Field(min_length=8, max_length=30)

class UserDelete(BaseModel):
    username: str = Field(max_length=50)
    password: str = Field(min_length=8, max_length=30)

class UserForDB(BaseUser):
    hashed_password: str

    class Config:
        orm_mode = True

class UserOut(BaseUser):
    pass

class Token(BaseModel):
    access_token: str
    token_type: str

class TokenData(BaseModel):
    username: str | None = None

