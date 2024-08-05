class Config:
    # 数据库配置
    DB_SETTINGS = {
        "DB_HOST": "192.168.1.123",
        "DB_NAME": "wj",
        "DB_USER": "xqs"
    }
    DB_CONN_STR = "postgresql+psycopg2://username:password@localhost/dbname"

    # REDIS数据库连接配置
    REDIS_SETTINGS = {

    }
    REDIS_CONN_STR = "redis://{CONFIG.REDIS_HOST}:{CONFIG.REDIS_PORT}/{CONFIG.REDIS_DB}"

    # DEBUG配置
    DEBUG = True

    # 修改代码后自动加载
    AUTO_RELOAD = True
