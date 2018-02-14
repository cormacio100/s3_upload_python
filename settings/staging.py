from base import *

DEBUG = False

SITE_URL = 'https://s3-upload-python.herokuapp.com'
ALLOWED_HOSTS.append('s3-upload-python.herokuapp.com')

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}

LOGGING = {
    'version':1,
    'disable_existing_loggerds': False,
    'handlers': {
        'console':{
            'class': 'logging.StreamHandler',
        },
    },
    'loggers': {
        'django': {
            'handlers': ['console'],
            'level': os.getenv('DJANGO_LOG_LEVEL','DEBUG')
        }
    }
}
