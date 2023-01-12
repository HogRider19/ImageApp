from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from config.config import TESTING_DB_NAME
from main import app

from .database import SQLALCHEMY_DATABASE_URL as DB_URL
from .database import Base, get_db

from fastapi.testclient import TestClient


SQLALCHEMY_TESTING_DATABASE_URL = DB_URL[:DB_URL.rindex('/')+1] + TESTING_DB_NAME

engine = create_engine(SQLALCHEMY_TESTING_DATABASE_URL)

TestingSessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base.metadata.create_all(bind=engine)

def get_testing_db():
    db_session = TestingSessionLocal()
    try:
        yield db_session
    finally:
        db_session.close()

client = None
if get_db in app.dependency_overrides:
    app.dependency_overrides[get_db] = get_testing_db
    client = TestClient(app)