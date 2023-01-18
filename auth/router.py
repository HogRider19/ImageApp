from fastapi import APIRouter, Depends, Form, HTTPException, status
from fastapi.security import OAuth2PasswordRequestForm
from sqlalchemy.orm import Session

from db.database import get_db

from .dependencies import get_curren_active_user
from .models import User
from .schemas import Token, UserCreate, UserForDB, UserOut
from .utils import (create_access_token, get_hashed_password,
                    get_user_by_username, verify_password)


auth_router = APIRouter(prefix='/auth', tags=['auth'])

@auth_router.post('/createuser', response_model=UserOut,
                    status_code=status.HTTP_201_CREATED)
async def create_user(user: UserCreate, db: Session = Depends(get_db)):
    username_db = db.query(User.username).filter(
                        User.username==user.username).first()
    if username_db is not None:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST,
                             detail='This username is already taken')

    db.add(User(
        username=user.username,
        email=user.email,
        hashed_password=get_hashed_password(user.password)))
    db.commit()
    return user

@auth_router.post('/login', response_model=Token)
async def login(
    login_form: OAuth2PasswordRequestForm = Depends(),
    db: Session = Depends(get_db)
):
    username = login_form.username
    password = login_form.password

    expected_user = get_user_by_username(username, db)

    if expected_user is None:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST, detail='Invalid username')

    if not verify_password(password, expected_user.hashed_password):
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST, detail='Invalid password')

    access_token = create_access_token({'sub': username})

    return {"access_token": access_token, "token_type": "bearer"}    


@auth_router.get('/me', response_model=UserOut)
async def me(user: UserForDB = Depends(get_curren_active_user)):
    return user