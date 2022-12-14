import os
import time
from pathlib import Path

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.1/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '=m2pzl4hm#5rym@0j$r^ma*8#@1tg_t=awzh)(v7iwn^v4d=qi'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ["*"]

# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'rest_framework',
    'corsheaders',
    'UserManage.apps.UsermanageConfig',
    'ArticleManage.apps.ArticlemanageConfig',
    'TagManage.apps.TagmanageConfig',
    'CategoryManage.apps.CategorymanageConfig',
    'CommonManage.apps.CommonmanageConfig',
    'QueryManage.apps.QuerymanageConfig'

]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'corsheaders.middleware.CorsMiddleware',
    'django.middleware.common.CommonMiddleware',
    # 'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'MiddleWares.BrowseMiddleware.SiteBrowseMiddleware',
    'MiddleWares.LoginTimeChangeMiddleware.TimeLinesChangeMiddleware',
]

ROOT_URLCONF = 'BlogSiteAdmin.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates')]
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

WSGI_APPLICATION = 'BlogSiteAdmin.wsgi.application'

# Database
# https://docs.djangoproject.com/en/3.1/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': "blog_admin",
        "USER": "root",
        "PASSWORD": "123456789",
        "HOST": "localhost",
        "PORT": 3306
    }
}

# Password validation
# https://docs.djangoproject.com/en/3.1/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/3.1/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = False

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.1/howto/static-files/

STATIC_URL = '/static/'

# ????????????
CORS_ALLOW_CREDENTIALS = True
CORS_ORIGIN_ALLOW_ALL = True
CORS_ALLOW_METHODS = (
    'DELETE',
    'GET',
    'OPTIONS',
    'PATCH',
    'POST',
    'PUT',
    'VIEW',
)
CORS_ALLOW_HEADERS = (
    'XMLHttpRequest',
    'X_FILENAME',
    'accept-encoding',
    'authorization',
    'content-type',
    'dnt',
    'origin',
    'user-agent',
    'x-csrftoken',
    'x-requested-with',
    'Pragma',
    'AUTHORIZATION'
)

# ????????????
cur_path = os.path.dirname(os.path.realpath(__file__))  # log_path????????????????????????
log_path = os.path.join(os.path.dirname(cur_path), 'logs')
if not os.path.exists(log_path):
    os.mkdir(log_path)  # ?????????????????????logs?????????????????????????????????
LOGGING = {
    'version': 1,
    'disable_existing_loggers': True,
    'formatters': {
        # ????????????
        'standard': {
            'format': '[%(asctime)s] [%(filename)s:%(lineno)d] [%(module)s:%(funcName)s] '
                      '[%(levelname)s]- %(message)s'},
        'simple': {  # ????????????
            'format': '%(levelname)s %(message)s'
        },
    },
    # ??????
    'filters': {
    },
    # ?????????????????????????????????
    'handlers': {
        # ????????????????????????
        'default': {
            'level': 'INFO',
            'class': 'logging.handlers.RotatingFileHandler',
            'filename': os.path.join(log_path, 'all-{}.log'.format(time.strftime('%Y-%m-%d'))),
            'maxBytes': 1024 * 1024 * 500,  # ????????????
            'backupCount': 5,  # ?????????
            'formatter': 'standard',  # ????????????
            'encoding': 'utf-8',  # ???????????????????????????????????????????????????
        },
        # ??????????????????
        # 'error': {
        #     'level': 'ERROR',
        #     'class': 'logging.handlers.RotatingFileHandler',
        #     'filename': os.path.join(log_path, 'error-{}.log'.format(time.strftime('%Y-%m-%d'))),
        #     'maxBytes': 1024 * 1024 * 5,  # ????????????
        #     'backupCount': 5,  # ?????????
        #     'formatter': 'standard',  # ????????????
        #     'encoding': 'utf-8',  # ??????????????????
        # },
        # ???????????????
        'console': {
            'level': 'DEBUG',
            'class': 'logging.StreamHandler',
            'formatter': 'standard'
        },
        # ??????info??????
        # 'info': {
        #     'level': 'INFO',
        #     'class': 'logging.handlers.RotatingFileHandler',
        #     'filename': os.path.join(log_path, 'info-{}.log'.format(time.strftime('%Y-%m-%d'))),
        #     'maxBytes': 1024 * 1024 * 5,
        #     'backupCount': 5,
        #     'formatter': 'standard',
        #     'encoding': 'utf-8',  # ??????????????????
        # },
    },
    # ?????????????????? handlers ???????????????
    'loggers': {
        # ?????? ??? django ?????????????????????????????? ????????????
        'django': {
            'handlers': ['default', 'console'],
            'level': 'INFO',
            'propagate': False
        },
        # log ?????????????????????????????????
        'log': {
            'handlers': ['console', 'default'],
            'level': 'INFO',
            'propagate': True
        },
    }
}

REST_FRAMEWORK = {
    "DEFAULT_AUTHENTICATION_CLASSES": ["Adapter.UserAuthenticate.UserAuthentication", ]
}
