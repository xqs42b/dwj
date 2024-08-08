import datetime
from uuid import uuid4
from apps.BaseModel import BaseModel, db


class UserModel(BaseModel):
    """用户数据模型"""
    __table__ = "user"

    username = db.Column(db.String(120), comment="用户名")
    phone = db.Column(db.String(11), comment="手机号")
    gender = db.Column(db.Boolean, default=0, comment="用户性别")
    head = db.Column(db.String(320), comment='用户头像')
    birthday = db.Column(db.Date, defautl=datetime.date.today(), comment="用户生日")
    profile = db.Column(db.String(120), comment="简介")
    uid = db.Column(db.String(36), comment="用户的uid")
