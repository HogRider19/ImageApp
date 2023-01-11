from config.config import DB_HOST, DB_NAME, DB_PASSWORD, DB_PORT, DB_USER, DB_DRIVER
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy import MetaData


SQLALCHEMY_DATABASE_URL = f"postgresql+{DB_DRIVER}://{DB_USER}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_NAME}"


engine = create_engine(SQLALCHEMY_DATABASE_URL)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()

metadata = MetaData()



