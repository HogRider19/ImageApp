import os
from uuid import uuid4

from fastapi import UploadFile
from sqlalchemy.orm import Session

from auth.models import User
from auth.schemas import UserForDB, UserOut
from config.config import MEDIA_BASE_DIR

from .models import Image
from .schemas import ImageForDb, ImageInfo


def save_image(
    image_file: UploadFile,
    info: ImageInfo,
    user: UserForDB,
    db: Session
) -> None:
    """Соханяет изображение в бд"""
    user_dir_name = f"{MEDIA_BASE_DIR}{user.username}"
    if not os.path.exists(user_dir_name):
        os.mkdir(user_dir_name)

    relative_file_path = f"{user.username}/{uuid4()}.jpeg"
    file_path = f"{MEDIA_BASE_DIR}{relative_file_path}"

    with open(file_path, mode='wb') as file:
        file.write(image_file.file.read())

    image_db = Image(
        title=info.title,
        description=info.description,
        path=relative_file_path,
        user_id=user.id,
    )

    db.add(image_db)
    db.commit()

def delete_image_completely(image: ImageForDb, db: Session) -> None:
    """Удаляет изображение из media и базы данных"""
    image_path = f"{MEDIA_BASE_DIR}{image.path}"
    if os.path.exists(image_path):
        os.remove(image_path)

    image_db = db.query(Image).get(image.id)
    db.delete(image_db)
    db.commit()

def get_user_images(user: UserForDB, db: Session) -> list[ImageForDb]:
    images_db = db.query(Image).filter(Image.user_id==user.id).all()
    return [convert_image_model(image_db) for image_db in images_db]

def get_image_info_by_id(id: int, db: Session) -> ImageForDb | None:
    """Возвращает информацию о картинке по ее id"""
    image = db.query(Image).join(User).filter(Image.id==id).first()
    if image:
        return convert_image_model(image)

def convert_image_model(image) -> ImageForDb:
    user_db = image.user
    user = UserOut(
        username = user_db.username,
        email=user_db.email,
        registed_at=user_db.registed_at,
        is_superuser=user_db.is_superuser,
        role_id=user_db.role_id)
        
    return ImageForDb(
        id=image.id,
        title=image.title,
        description=image.description,
        created_at=image.created_at,
        path=image.path,
        liks=image.liks,
        user=user,)

