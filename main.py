from fastapi import FastAPI, Request
from auth.router import auth_router
from api.router import api_router
from config.config import MEDIA_BASE_DIR, TESTING_MEDIA_BASE_DIR, DEBUG
import os
from config.logging import get_logger


logger = get_logger(__name__)

app = FastAPI(
    title='ImageApp',
)

app.include_router(auth_router)
app.include_router(api_router)


@app.on_event("startup")
def startup_event():
    if not os.path.exists(MEDIA_BASE_DIR):
        os.mkdir(MEDIA_BASE_DIR)




