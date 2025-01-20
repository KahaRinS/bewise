from settings.base import env


class DbConfig:
    CONNECTION_SETTINGS = {
        'dsn': env.str('DB_URL', default='postgresql+asyncpg://postgres:postgres@0.0.0.0:5432/postgres'),
    }
