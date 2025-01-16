from settings.base import env


class DBConfig:
    POSTGRES_HOST = env.str('POSTGRES_HOST', default='localhost')
    POSTGRES_PORT = env.int('POSTGRES_PORT', default=5432)  # Noqa: WPS432
    DB_NAME = env.str('DB_NAME', default='postgres')
    POSTGRES_USER = env.str('POSTGRES_USER', default='postgres')
    POSTGRES_PASSWORD = env.str('POSTGRES_PASSWORD', default='root')

    DATABASE_URL = (
        f'postgresql+asyncpg://{POSTGRES_USER}:{POSTGRES_PASSWORD}'
        f'@{POSTGRES_HOST}:{POSTGRES_PORT}/{DB_NAME}'  # Noqa: WPS326
    )
