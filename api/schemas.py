from pydantic import BaseModel, Field
from auth.schemas import UserOut
import datetime


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

class ImageInfo(BaseImage):
    pass


