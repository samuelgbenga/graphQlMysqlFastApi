
from dotenv import load_dotenv
from sqlalchemy import create_engine, MetaData
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
import os

load_dotenv()

DATABASE_URL: str  = os.getenv("DATABASE_URL") # type: ignore


engine = create_engine(DATABASE_URL)

SessionLocal = sessionmaker(autoflush=False, bind=engine)

Base = declarative_base()

meta = MetaData()


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
