from pydantic import BaseModel, Field
import datetime


class Role(BaseModel):
    id: int
    name: str

class BaseUser(BaseModel):
    username: str = Field(max_length=50)
    email: str = Field(max_length=100)
    registed_at: datetime.datetime
    is_superuser: bool
    role_id: int

class UserIn(BaseModel):
    password: str = Field(min_length=8, max_length=30)

class UserForDB(BaseModel):
    hashed_password: str

    class Config:
        orm_mode = True

class UserOut(BaseModel):
    pass

class Token(BaseModel):
    access_token: str
    token_type: str

class TokenData(BaseModel):
    username: str | None = None

