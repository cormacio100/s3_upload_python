from base import *

DEBUG = True

# Database
# https://docs.djangoproject.com/en/1.11/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}

LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'formatters': {
        'details': {
            'format': '%(process)d %(filename)s %(funcName)s %(levelname)s %(lineno)d %(message)s',
        },
    },
    'handlers': {
        'file': {
            'level': 'DEBUG',
            'class': 'logging.FileHandler',
            'filename': 'debug.log',
            'formatter': 'details'
        },
    },
    'loggers': {
        'accounts.views': {
            'handlers': ['file'],
            'level': 'DEBUG',
            'propagate': True
        },
    }
}

