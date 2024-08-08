import sqlalchemy as db
from datetime import datetime
from sqlalchemy.orm import declarative_base


Base = declarative_base()


class BaseModel(Base):
    __abstract__ = True

    id = db.Column(db.Integer, primary_key=True, comment='序号')
    add_time = db.Column(db.DateTime, default=datetime.now(), comment='添加时间')
    update_time = db.Column(db.DateTime, default=datetime.now(), comment='修改时间')
