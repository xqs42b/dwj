from sanic import Blueprint
from sanic.response import json
from uuid import uuid4
from pydantic import BaseModel, field_validator
from datetime import date
from typing import Optional


login_bp = Blueprint("login_blueprint")


class User(BaseModel):
    """用户字段认证"""
    username: str
    password: str
    phone: str
    gender: bool
    head: Optional[str] = None
    birthday: Optional[date] = None
    profile: Optional[str] = None

    @field_validator('phone')
    def check_phone(cls, phone_val):
        if isinstance(phone_val, str) and not phone_val.isdigit():
            raise ValueError("the phone number can only be a number")
        if len(phone_val) != 11:
            raise ValueError("the phone number must be 11 digits long")
        return phone_val


@login_bp.post("/login")
async def login(request):
    pass


@login_bp.post("/register")
async def register(request):
    pass
