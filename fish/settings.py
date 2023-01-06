
import os
from pathlib import Path


BASE_DIR = Path(__file__).resolve().parent.parent





SECRET_KEY = 'django-insecure-isi!#3_*^%^ium1b&j+gl+0w!vo@3__spj_0&%1s0@_ebs=u*v'


DEBUG = False

ALLOWED_HOSTS = [
    '45.142.122.154',
    'stikkerss.ru',
    '127.0.0.1'
]





INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'authors.apps.AuthorsConfig',
    'django_user_agents',
    'stikers.apps.StikersConfig'


]




MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'django_user_agents.middleware.UserAgentMiddleware',
]

ROOT_URLCONF = 'fish.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR / 'templates']
        ,
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

WSGI_APPLICATION = 'fish.wsgi.application'



DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'HOST': '92.53.120.60',
        'NAME': 'default_db',
        'USER': 'gen_user',
        'PASSWORD': 'zszr3zwr99',
        'CONN_MAX_AGE': 31500000,
        'PORT': '3306',
        'OPTIONS': {
            'charset': 'utf8mb4',
            "init_command": "SET foreign_key_checks=0;"
                            "SET NAMES 'utf8mb4';"
                            "SET SESSION collation_connection = 'utf8mb4_unicode_ci';",
        }
    },
}





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




LANGUAGE_CODE = 'ru-en'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True




STATIC_ROOT = os.path.join(BASE_DIR, "static")

STATIC_URL = '/static/'



DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'
