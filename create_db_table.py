import asyncio
from apps.BaseModel import Base
from config import Config
from sqlalchemy.ext.asyncio import create_async_engine


async def main():
    engine = create_async_engine(Config.DB_CONN_STR, echo=True)

    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)


if __name__ == "__main__":
    loop = asyncio.get_event_loop()
    loop.run_until_complete(main())