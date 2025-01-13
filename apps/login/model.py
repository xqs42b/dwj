import datetime
from apps.BaseModel import BaseModel, db, Base


class UserModel(BaseModel):
    """用户数据模型"""
    __tablename__ = "user"

    username = db.Column(db.String(120), comment="用户名")
    password = db.Column(db.VARCHAR(120), comment="密码")
    phone = db.Column(db.String(11), comment="手机号")
    gender = db.Column(db.Boolean, default=0, comment="用户性别")
    head = db.Column(db.String(320), comment='用户头像')
    birthday = db.Column(db.Date, default=datetime.date.today, comment="用户生日")
    profile = db.Column(db.String(120), comment="简介")
    uid = db.Column(db.String(32), comment="用户的uid")

import asyncio
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
