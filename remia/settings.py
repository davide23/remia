"""
Django settings for remia project.

Generated by 'django-admin startproject' using Django 2.0.6.

For more information on this file, see
https://docs.djangoproject.com/en/2.0/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/2.0/ref/settings/
"""

import os
import environ

os.environ['DJANGO_SETTINGS_MODULE'] = 'remia.settings'

ROOT_DIR = environ.Path(__file__) - 3  # (/a/b/myfile.py - 3 = /)

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
TEMPLATE_PATH = os.path.join(BASE_DIR, 'remia/shippings/templates')

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/2.0/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '+=or+6vx58zpp)#4b(8=w1t1arq=x)dd@09n5!l_ar4v+-+@!y'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = False

ALLOWED_HOSTS = ['*']
#
# STATICFILES_DIRS = (
#     os.path.join(BASE_DIR, "shippings/static"),
#     '/var/www/static/',
# )
# Application definition
INSTALLED_APPS = [
    'shippings',
    'crispy_forms',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django_extensions',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'remia.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [TEMPLATE_PATH],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'remia.wsgi.application'

# CLOUD_STORAGE_BUCKET = os.environ['CLOUD_STORAGE_BUCKET']

# Deploying DB
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'remiaclients',
        'USER': 'postgres',
        'PASSWORD': 'free_to_enter',
        'HOST': '/cloudsql/remia012:europe-west4:remiaclients',
        'PORT': '5432',
    }
}

# Running on production App Engine, so use a Google Cloud SQL database.
# DATABASES = {
#         'default': {
#             'ENGINE': 'django.db.backends.postgresql',
#             'HOST': '/cloudsql/remia012:europe-west4:remiaclients',
#             'NAME': 'remiaclients',
#             'USER': 'postgres',
#             'PASSWORD': 'free_to_enter',
#             'PORT': '5432',
#         }
#     }
# Local
# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.postgresql',
#         'NAME': 'remiaclients',
#         'USER': 'postgres',
#         'PASSWORD': 'free_to_enter',
#     }
# }
# # [END dbconfig]

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True

# Password validation
# https://docs.djangoproject.com/en/2.0/ref/settings/#auth-password-validators
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

# [START staticurl]
# Fill in your cloud bucket and switch which one of the following 2 lines
# is commented to serve static content from GCS
# STATIC_URL = 'https://storage.googleapis.com/remia-static/staticfiles/'
STATIC_URL = 'https://storage.googleapis.com/remia/static/'
# STATIC_URL = '/static/'
# STATIC_ROOT = 'static/'
# import ipdb
# ipdb.set_trace(){%

# STATICFILES_DIRS = [
#     os.path.join(BASE_DIR, "static"),
#     '/static/',
# ]
# See: https://docs.djangoproject.com/en/dev/ref/settings/#static-root
STATIC_ROOT = str(ROOT_DIR + 'remia/staticfiles')

# See: https://docs.djangoproject.com/en/dev/ref/settings/#static-url
# STATIC_URL = '/static/'

# See: https://docs.djangoproject.com/en/dev/ref/contrib/staticfiles/#std:setting-STATICFILES_DIRS
STATICFILES_DIRS = (
    str(BASE_DIR + '/static'),
)

# See: https://docs.djangoproject.com/en/dev/ref/contrib/staticfiles/#staticfiles-finders
STATICFILES_FINDERS = (
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
)
