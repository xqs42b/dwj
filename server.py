import os
from sanic import Sanic
from sanic.response import text
from config import Config


exec_path = os.path.dirname(__file__)
config_name = "config.py"
config_path = f"{exec_path}/{config_name}"
print(config_path)

app = Sanic("myApp")
app.update_config(Config)
print(app.config.A)
print(app.config.DB_SETTINGS)

@app.get("/")
async def hi(request):
    return text("hi china")
