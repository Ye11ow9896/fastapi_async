from envparse import Env
from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession
from sqlalchemy.orm import sessionmaker

env = Env()

REAL_DATABASE_URL = env.srt(
    "REAL_DATABASE_URL",
    default='postgres+asyncpg://postrgres:postgres@127.0.0.1:5432/test_async'
)

engine = create_async_engine(REAL_DATABASE_URL, future=True, echo=True)
async_session = sessionmaker(engine, expire_on_commit=False, class_=AsyncSession)