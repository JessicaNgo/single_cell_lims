"""
Django settings for elastidjango project.

Generated by 'django-admin startproject' using Django 1.9.6.

For more information on this file, see
https://docs.djangoproject.com/en/1.9/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.9/ref/settings/

Created on May 16, 2016
@author: Jafar Taghiyar (jtaghiyar@bccrc.ca)
"""

import os
import sys

# Version
VERSION = "1.0.0"

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# Export apps to PYTHONPATH
sys.path.append(os.path.join(BASE_DIR, 'apps'))

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.9/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = ''

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []
HOST_URL = ''

# Application definition

INSTALLED_APPS = [
    'core.apps.CoreConfig', 
    'account.apps.AccountConfig', 
    'khayyam.apps.KhayyamConfig',
    'picasso.apps.PicassoConfig',
    'taggit',
    'simple_history',
    # 'bootstrap3',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    # 'mod_wsgi.server',
]

MIDDLEWARE_CLASSES = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.auth.middleware.SessionAuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'simple_history.middleware.HistoryRequestMiddleware',
]

ROOT_URLCONF = 'elastidjango.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [
                 os.path.join(BASE_DIR, 'templates')],
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

WSGI_APPLICATION = 'elastidjango.wsgi.application'


# Database
# https://docs.djangoproject.com/en/1.9/ref/settings/#databases

# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.sqlite3',
#         'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
#     }
# }

DATABASES = {
    'default': {
        # for older django versions use ".postgresql_psycopg2"
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': '',
        'USER': '',
        'PASSWORD': '',
        'HOST': '',
        'PORT': '',
    }
}


# Password validation
# https://docs.djangoproject.com/en/1.9/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/1.9/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'US/Pacific'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.9/howto/static-files/

STATIC_URL = '/static/'

# STATICDILES_DIR = []

STATIFILES_FINDERS = [
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
]
STATIC_ROOT = os.path.join(os.path.dirname(BASE_DIR), "static_cdn") 

# Media files
MEDIA_URL = "/media/"
MEDIA_ROOT = os.path.join(os.path.dirname(BASE_DIR), "uploads")

# Login url
LOGIN_URL = '/apps/account/login/'

#=======================
# Inegration settings
#-----------------------
# archives
DATA_ARCHIVE = '/genesis/shahlab/IDAP/DATA_ARCHIVE'
RESULTS_ARCHIVE = '/genesis/shahlab/IDAP/RESULTS_ARCHIVE'
WORKFLOWS_ARCHIVE = '/genesis/shahlab/IDAP/WORKFLOWS_ARCHIVE'

# working env
KRONOS_PYTHON_VENV = '/genesis/shahlab/IDAP/VENV/kronos_2.3.1_dev/bin/activate'
WORKING_DIR_ROOT = '/genesis/shahlab/IDAP/WD_ROOT'

#=======================
# Celery configuration
#-----------------------
from kombu import Exchange, Queue
CELERY_QUEUES = (
    Queue('celery', Exchange('celery'), routing_key='celery'),
    Queue('workflow_run', Exchange('workflow_run'), routing_key='workflow_run'),
    Queue('workflow_stop', Exchange('workflow_stop'), routing_key='workflow_stop'),
)

CELERY_ROUTES = {
    'khayyam.tasks.run_workflow': {'queue': 'workflow_run', 'routing_key': 'workflow_run'},
    'khayyam.tasks.stop_workflow': {'queue': 'workflow_stop', 'routing_key': 'workflow_stop'},
}

#=========================
# Email configuration
#-------------------------
EMAIL_ADDRESS = ""
EMAIL_PASSWORD = ""
SMTP_SERVER = ""
SMTP_PORT = 0

#=========================
# Genesis cluster settings
#-------------------------
QCMD_PREFIX = ''
SGE_ROOT = ''
SGE_QMASTER_PORT = ''
SGE_EXECD_PORT = ''
SGE_CELL = ''
