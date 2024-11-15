import sqlite3

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from settings import Settings

settings = Settings()

engine = create_engine(
    f'postgresql+psycopg2://{settings.DB_USER}:{settings.DB_PASSWORD}@{settings.DB_HOST}:{settings.DB_PORT}/{settings.DB_NAME}'
)

Session = sessionmaker(engine)


def get_db_connection() -> sqlite3.Connection:
    return sqlite3.connect(settings.sqlite_db_name)


def get_db_session() -> Session:
    return Session
