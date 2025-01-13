import asyncio
from apps.BaseModel import Base
from config import Config
from sqlalchemy.ext.asyncio import create_async_engine, AsyncEngine


async def main():
    engine: AsyncEngine = create_async_engine(Config.DB_CONN_STR, echo=True)

    async with engine.begin() as conn:
        print("start create table!")
        await conn.run_sync(Base.metadata.create_all)
        print("tables created")


if __name__ == "__main__":
    asyncio.run(main())
