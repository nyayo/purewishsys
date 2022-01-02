"""
Django settings for purewishsys project.

Generated by 'django-admin startproject' using Django 3.2.7.

For more information on this file, see
https://docs.djangoproject.com/en/3.2/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/3.2/ref/settings/
"""

from pathlib import Path
import os

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-1taf8@0403=%wm9g990&t1h=_ewui-yi#^adds5mt5#@i26n6d'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ["*"]


# Application definition

INSTALLED_APPS = [
    'channels',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'widget_tweaks',
    'purewish',
    'postman',
    'chat',
    'crispy_forms',
    # 'django_private_chat',
]
AUTH_USER_MODEL = "auth.User"


# POSTMAN_I18N_URLS = True  # default is False
# POSTMAN_DISALLOW_ANONYMOUS = True  # default is False
# POSTMAN_DISALLOW_MULTIRECIPIENTS = False  # default is False
# POSTMAN_DISALLOW_COPIES_ON_REPLY = True  # default is False
# POSTMAN_DISABLE_USER_EMAILING = True  # default is False
# POSTMAN_FROM_EMAIL = 'from@host.tld'  # default is DEFAULT_FROM_EMAIL
# POSTMAN_PARAMS_EMAIL = get_params_email  # default is None
POSTMAN_AUTO_MODERATE_AS = True  # default is None
# POSTMAN_SHOW_USER_AS = 'get_full_name'  # default is None
# POSTMAN_NAME_USER_AS = 'first_name'  # default is None
# POSTMAN_QUICKREPLY_QUOTE_BODY = True  # default is False
# POSTMAN_NOTIFIER_APP = None  # default is 'notification'
# POSTMAN_MAILER_APP = None  # default is 'mailer'
# POSTMAN_AUTOCOMPLETER_APP = {
# 'name': '',  # default is 'ajax_select'
# 'field': '',  # default is 'AutoCompleteField'
# 'arg_name': '',  # default is 'channel'
# 'arg_default': 'postman_friends',  # no default, mandatory to enable the feature
# }  # default is {}


MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'purewishsys.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR / 'templates'],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
                'postman.context_processors.inbox',
            ],
        },
    },
]

use_websockets = True

WSGI_APPLICATION = 'purewishsys.wsgi.application'
ASGI_APPLICATION = 'purewishsys.asgi.application'

CHANNEL_LAYERS = {
    'default': {
        'BACKEND': 'channels_redis.core.RedisChannelLayer',
        'CONFIG': {
            "hosts": [('127.0.0.1', 6379)]
        }
    }
}


# Database
# https://docs.djangoproject.com/en/3.2/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'money',
        'USER': 'rooting',
        'PASSWORD': 'rooting',
        'PORT': '3300',
        'TEST': {
            'NAME': 'mytest'
        }
    }
    # 'default': {
    #     'ENGINE': 'django.db.backends.sqlite3',
    #     'NAME': BASE_DIR / 'db.sqlite3',
    # }
}


# Password validation
# https://docs.djangoproject.com/en/3.2/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]


# Internationalization
# https://docs.djangoproject.com/en/3.2/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.2/howto/static-files/

STATIC_URL = '/static/'

MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')

# Default primary key field type
# https://docs.djangoproject.com/en/3.2/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_PORT = 587
EMAIL_HOST_USER = 'ivannyayo@gmail.com'
EMAIL_HOST_PASSWORD = 'passcode02'
EMAIL_USE_TLS = True
EMAIL_USE_SSL = False

LOGIN_REDIRECT_URL = 'login'

LOGIN_URL = 'login'


# CHAT_WS_SERVER_HOST = '127.0.0.1'
# CHAT_WS_SERVER_PORT = 5002
# CHAT_WS_SERVER_PROTOCOL = 'ws'
