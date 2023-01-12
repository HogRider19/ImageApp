from config.config import DB_HOST, DB_NAME, DB_PASSWORD, DB_PORT, DB_USER, DB_DRIVER
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from config.logging import get_logger


logger = get_logger(__name__)


SQLALCHEMY_DATABASE_URL = f"postgresql+{DB_DRIVER}://{DB_USER}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_NAME}"

engine = create_engine(SQLALCHEMY_DATABASE_URL)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()

def get_db():
    db_session = SessionLocal()
    try:
        yield db_session
    except Exception as exc:
        logger.error('%s', exc)
        raise exc
    finally:
        db_session.close()



