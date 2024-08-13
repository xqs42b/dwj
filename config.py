class Config:
    # 数据库配置
    DB_HOST = "192.168.138.128"
    DB_PORT = "5432"
    DB_USER = "xqs"
    DB_PASSWORD = "123456"
    DB_NAME = "dwj"
    DB_CONN_STR = f"postgresql+asyncpg://{DB_HOST}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_NAME}"

    # REDIS数据库连接配置
    REDIS_HOST = "192.168.138.128"
    REDIS_PORT = "6379"
    REDIS_DB = 0
    REDIS_CONN_STR = f"redis://{REDIS_HOST}:{REDIS_PORT}/{REDIS_DB}"

    # DEBUG配置
    DEBUG = True

    # 修改代码后自动加载
    AUTO_RELOAD = True
