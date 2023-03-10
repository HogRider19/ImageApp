import os

from fastapi import (APIRouter, BackgroundTasks, Depends, File, Form,
                     HTTPException, Query, UploadFile, status)
from fastapi.responses import FileResponse
from sqlalchemy.orm import Session

from auth.dependencies import get_curren_active_user
from auth.schemas import UserForDB
from config.config import MEDIA_BASE_DIR
from config.logging import get_logger
from db.database import get_db

from .schemas import ImageForDb, ImageInfo
from .utils import (delete_image_completely, get_image_info_by_id,
                    get_limit_offset, get_popular_images_from_db,
                    get_user_images, save_image)

logger = get_logger(__name__)

api_router = APIRouter(tags=['images'])

@api_router.post('/image/load', response_model=ImageInfo)
def load_image(
    backgroundtasks: BackgroundTasks,
    title: str = Form(max_length=100),
    desc: str = Form(default=None, max_length=1000),
    image_file: UploadFile = File(...),
    user: UserForDB = Depends(get_curren_active_user),
    db: Session = Depends(get_db),
):
    image_info = ImageInfo(title=title, description=desc)
    if image_file.content_type not in ['image/jpeg', 'image/png']:
        raise HTTPException(
            status_code=status.HTTP_415_UNSUPPORTED_MEDIA_TYPE,
            detail='Content type must be jpeg or png')

    backgroundtasks.add_task(save_image, image_file, image_info, user, db)

    return image_info

@api_router.delete('/image/deleta/{image_id}', response_model=ImageInfo)
def delete_image(
    image_id: int,
    db: Session = Depends(get_db),
    user: UserForDB = Depends(get_curren_active_user)
):    
    image_info = get_image_info_by_id(image_id, db)
    if not image_info:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                detail=f"Image with id-{image_id} does not exist")

    if image_info.user.username != user.username:
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN,
                detail=f"You are not the author of this image")

    delete_image_completely(image_info, db)
    return image_info

@api_router.get('/image/popular', response_model=list[ImageForDb])
def get_popular_images(
    page: int = Query(default=0, ge=0),
    page_size: int = Query(default=10, gt=0, lt=100),
    db: Session = Depends(get_db),
    user: UserForDB = Depends(get_curren_active_user),
):  
    limit, offset = get_limit_offset(page, page_size)
    images = get_popular_images_from_db(limit, offset,  db)
    return images

@api_router.get('/image/{image_id}', response_model=ImageForDb)
def get_image_info(
    image_id: int,
    db: Session = Depends(get_db),
    user: UserForDB = Depends(get_curren_active_user)
):  
    image_info = get_image_info_by_id(image_id, db)
    if not image_info:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                detail=f"Image with id-{image_id} does not exist")

    return image_info

@api_router.get('/images/my', response_model=list[ImageForDb])
def get_my_images(
    page: int = Query(default=0, ge=0),
    page_size: int = Query(default=10, gt=0, lt=100),
    db: Session = Depends(get_db),
    user: UserForDB = Depends(get_curren_active_user),
):
    limit, offset = get_limit_offset(page, page_size)
    return get_user_images(user, db, limit, offset)

@api_router.get('/media/{username}/{image_name}', response_class=FileResponse)
def get_image(
    username: str,
    image_name: str,
    user: UserForDB = Depends(get_curren_active_user)
):
    file_path = f"{MEDIA_BASE_DIR}{username}/{image_name}"
    if not os.path.exists(file_path):
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Invalid image path")

    return FileResponse(path=file_path, media_type='image/jpeg')




