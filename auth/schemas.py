from pydantic import BaseModel
import datetime


class Role(BaseModel):
    id: int
    name: str

class BaseUser(BaseModel):
    username: str
    email: str
    registed_at: datetime.datetime
    is_superuser: bool
    role_id: Role

class UserIn(BaseModel):
    password: str

class UserForDB(BaseModel):
    hashed_password: str

class UserOut(BaseModel):
    pass

