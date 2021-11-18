"""
PRODUCTION MODE CONFIGURATION
"""
from . import settings
import environ
import os
from pathlib import Path


SUPPORTED_NONLOCALES = ['media', 'admin', 'static']

# Build paths inside the project like this: BASE_DIR / 'subdir'.
PROJECT_ROOT = os.path.abspath(os.path.dirname(__file__) + "../../../")


env = environ.Env()
# reading .env file
environ.Env.read_env()

env = environ.Env(
    # set casting, default value
    DEBUG=(bool, True)
)

PROJECT_ROOT = os.path.abspath(os.path.dirname(__file__) + "../../../")

environ.Env.read_env(os.path.join(PROJECT_ROOT, '.env'))


SECRET_KEY = env("SECRET_KEY", default="unsafe-secret-key")

DEBUG = env('DEBUG')

## Log settings
# Remove this configuration variable to use your custom logging configuration
DJANGO_LOG_LEVEL= DEBUG

LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'handlers': {
        'console': {
            'class': 'logging.StreamHandler',
        },
    },
    'root': {
        'handlers': ['console'],
        'level': 'WARNING',
    },
    'loggers': {
        'django': {
            'handlers': ['console'],
            'level': os.getenv('DJANGO_LOG_LEVEL', 'INFO'),
            'propagate': False,
        },
    },
}
