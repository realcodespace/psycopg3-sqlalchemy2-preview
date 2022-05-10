from sqlalchemy import create_engine
from sqlalchemy.ext.asyncio import create_async_engine


db_string = "postgresql+psycopg://user:password@db/psycoptest"

engine = create_engine(db_string)
async_engine = create_async_engine(db_string)
