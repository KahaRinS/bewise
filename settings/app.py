from .base import env

DEFAULT_PORT = 8000


class AppConfig:
    HOST = env.str('HOST', default='0.0.0.0')
    PORT = env.int('PORT', default=DEFAULT_PORT)
    VERSION = env.str('VERSION', default='local')
    DEBUG = env.bool('DEBUG', default=False)
    PROJECT_NAME = env.str('PROJECT_NAME', default='bewise')

    CORS = {
        'allow_headers': tuple(env.list('APP_ALLOW_HEADERS', default=['*'])),
        'expose_headers': tuple(env.list('APP_EXPOSE_HEADERS', default=['*'])),
        'allow_credentials': env.bool('APP_ALLOW_CREDENTIALS', default=False),
        'max_age': env.int('APP_MAX_AGE', default=0),
    }
