"""
Django settings for athena_devel project.

For more information on this file, see
https://docs.djangoproject.com/en/1.6/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.6/ref/settings/
"""

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import os
BASE_DIR = os.path.dirname(os.path.dirname(__file__))

from configurations import Configuration

from athena_devel import local_settings


class Base(Configuration):
    # SECURITY WARNING: don't run with debug turned on in production!
    DEBUG = False

    TEMPLATE_DEBUG = False

    ALLOWED_HOSTS = ['*']

    # Application definition

    EXTERNAL_APPS = (
        'django.contrib.admin',
        'django.contrib.auth',
        'django.contrib.contenttypes',
        'django.contrib.sessions',
        'django.contrib.messages',
        'django.contrib.staticfiles',
    )

    INTERNAL_APPS = (
        'athena',
    )

    INSTALLED_APPS = EXTERNAL_APPS + INTERNAL_APPS


    MIDDLEWARE_CLASSES = (
        'django.contrib.sessions.middleware.SessionMiddleware',
        'django.middleware.common.CommonMiddleware',
        'django.middleware.csrf.CsrfViewMiddleware',
        'django.contrib.auth.middleware.AuthenticationMiddleware',
        'django.contrib.messages.middleware.MessageMiddleware',
        'django.middleware.clickjacking.XFrameOptionsMiddleware',
    )

    ROOT_URLCONF = 'athena_devel.urls'

    WSGI_APPLICATION = 'athena_devel.wsgi.application'

    USE_I18N = True

    USE_L10N = True

    USE_TZ = True

    LANGUAGE_CODE = 'en-us'

    TIME_ZONE = local_settings.TIME_ZONE

    SECRET_KEY = local_settings.SECRET_KEY

    DATABASES = local_settings.DATABASES

    STATIC_URL = local_settings.STATIC_URL
    STATIC_ROOT = local_settings.STATIC_ROOT

    MEDIA_URL = local_settings.MEDIA_URL
    MEDIA_ROOT = local_settings.MEDIA_ROOT


class Prod(Base):
    pass


class Dev(Base):
    DEBUG = True
    TEMPLATE_DEBUG = True