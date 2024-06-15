from sqlalchemy import NullPool
from sqlalchemy.ext.asyncio import AsyncSession, create_async_engine
from sqlalchemy.orm import DeclarativeBase, sessionmaker

import os
from dotenv import load_dotenv

load_dotenv()
DB_USER = os.getenv('DB_USER')
DB_PASS = os.getenv('DB_PASS')
DB_HOST = os.getenv('DB_HOST')
DB_PORT = os.getenv('DB_PORT')
DB_NAME = os.getenv('DB_NAME')

DATABASE_URL = f'postgresql+asyncpg://{DB_USER}:{DB_PASS}@{DB_HOST}:{DB_PORT}/{DB_NAME}'
DATABASE_PARAMS = {'poolclass': NullPool}

engine = create_async_engine(DATABASE_URL, **DATABASE_PARAMS)

async_session_maker = sessionmaker(engine,
                                   class_=AsyncSession,
                                   expire_on_commit=False)

class Base(DeclarativeBase):
    pass