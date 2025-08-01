from .base import *


# Database
# https://docs.djangoproject.com/en/5.2/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}


# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-5u&y@^gawn!g36yti@_v8*+!lm4gn2gr3*ww5$4%j&2bpk@v4+'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ['*']