from base import *
import dj_database_url

DEBUG = False

SITE_URL = 'https://s3-upload-python.herokuapp.com'
ALLOWED_HOSTS.append('s3-upload-python.herokuapp.com')

DATABASES = {
    'default': dj_database_url.config('CLEARDB_DATABASE_URL')
}

LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'handlers': {
        'console': {
            'class': 'logging.StreamHandler',
        },
    },
    'loggers': {
        'django': {
            'handlers': ['console'],
            'level': os.getenv('DJANGO_LOG_LEVEL', 'DEBUG'),
        },
        'accounts': {
            'handlers': ['console'],
            'level': os.getenv('DJANGO_LOG_LEVEL', 'DEBUG'),
        },
    },
}