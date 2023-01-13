from pydantic import BaseModel, Field


class ImageInfo(BaseModel):
    title: str
    description: str

    class Coonfig:
        orm_mode = True

