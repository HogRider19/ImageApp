from sqlalchemy.orm import Session
from fastapi import UploadFile
import aiofiles


async def save_image(image_file: UploadFile, db: Session):
    """Соханяет изображение в бд"""
    pass