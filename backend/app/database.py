import os
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base

# SQLite database setup: database file will be created locally as crop_system.db
SQLALCHEMY_DATABASE_URL = "sqlite:///./crop_system.db"

# connect_args={"check_same_thread": False} is required for SQLite in multi-threaded FastAPI
engine = create_engine(
    SQLALCHEMY_DATABASE_URL, connect_args={"check_same_thread": False}
)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()

# Dependency to get database session per request
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()