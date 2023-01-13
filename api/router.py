from fastapi import (APIRouter, BackgroundTasks, File, Form, HTTPException,
                     UploadFile, status, Depends)

from .schemas import ImageInfo
from .utils import save_image

from db.database import get_db
from sqlalchemy.orm import Session

from auth.dependencies import get_curren_active_user
from auth.schemas import UserForDB


api_router = APIRouter(tags=['images'])

@api_router.post('/image/load', response_model=ImageInfo)
async def load_image(
    backgroundtasks: BackgroundTasks,
    title: str = Form(max_length=100),
    desc: str = Form(max_length=1000),
    image_file: UploadFile = File(...),
    user: UserForDB = Depends(get_curren_active_user),
    db: Session = Depends(get_db),
):
    image_info = ImageInfo(title=title, description=desc)
    if image_file.content_type not in ['image/jpeg', 'image/png']:
        raise HTTPException(
            status_code=status.HTTP_415_UNSUPPORTED_MEDIA_TYPE,
            detail='Content type must be jpeg or png')

    backgroundtasks.add_task(save_image, image_file=image_file, db=db)
    return ImageInfo


@api_router.post('image/{image_id}')
def get_iamge(image_id: int):
    pass