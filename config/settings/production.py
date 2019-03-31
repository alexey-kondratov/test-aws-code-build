from .common import *  # noqa

DEBUG = False
ENVIRONMENT = 'production'

DATABASES = {
    'default': {
        'ENGINE': 'django.contrib.gis.db.backends.postgis',
        'NAME': '%DB_NAME%',
        'USER': '%DB_USER%',
        'PASSWORD': '%DB_PASSWORD%',
        'HOST': '%DB_HOST%',
        'PORT': '%DB_PORT%',
    }
}

ACCOUNT_EMAIL_VERIFICATION = 'mandatory'


INSTALLED_APPS += (
)
