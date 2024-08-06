import os
import aioredis
from sanic import Sanic
from sanic.response import text
from config import Config
from contextvars import ContextVar
from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession
from sqlalchemy.orm import sessionmaker


exec_path = os.path.dirname(__file__)
config_name = "config.py"
config_path = f"{exec_path}/{config_name}"
print(config_path)

app = Sanic("myApp")
app.update_config(Config)
print(app.config.A)
print(app.config.DB_SETTINGS)


_base_model_session_ctx = ContextVar("session")


bind = create_async_engine(Config.DB_SETTINGS, echo=True, pool_size=500, max_overflow=1000)
_sessionmaker = sessionmaker(bind, class_=AsyncSession, expire_on_commit=False)


@app.listener("before_server_start")
async def setup_db(app):
    app.ctx.redis = aioredis.from_url(Config.REDIS_CONN_STR)


@app.middleware("request")
async def inject_session(request):
    request.ctx.session = _sessionmaker()
    request.ctx.session_ctx_token = _base_model_session_ctx.set(request.ctx.session)


@app.middleware("request")
async def close_session(request, response):
    if hasattr(request.ctx, "session_ctx_token"):
        _base_model_session_ctx.reset(request.ctx.session_ctx_token)
        await request.ctx.session.close()


@app.get("/")
async def hi(request):
    print("---------------request:", request)
    print(dir(request))
    print(request.id)
    return text("hi china")
