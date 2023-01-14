from sqlalchemy.orm import Session
from fastapi import UploadFile
from uuid import uuid4
from .schemas import ImageInfo
from auth.schemas import UserForDB
from config.config import MEDIA_BASE_DIR
from .models import Image
import aiofiles
import os



async def save_image(
    image_file: UploadFile,
    info: ImageInfo,
    user: UserForDB,
    db: Session
):
    """Соханяет изображение в бд"""
    user_dir_name = f"{MEDIA_BASE_DIR}{user.username}"
    if not os.path.exists(user_dir_name):
        os.mkdir(user_dir_name)

    file_path = f"{user_dir_name}/{uuid4()}.jpeg"

    with open(file_path, mode='wb') as file:
        file.write(image_file.file.read())


    image_db = Image(
        title=info.title,
        description=info.description,
        path=file_path,
        user_id=user.id,
    )

    db.add(image_db)
    db.commit()