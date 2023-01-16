import datetime

from pydantic import BaseModel

from auth.schemas import UserOut


class BaseImage(BaseModel):
    title: str
    description: str

    class Coonfig:
        orm_mode = True

class ImageForDb(BaseImage):
    id: int
    created_at: datetime.datetime
    liks: int
    path: str
    user: UserOut

class ImageInfo(BaseImage):
    pass


