"""
Django settings for property_passport project.

Generated by 'django-admin startproject' using Django 2.2.1.

For more information on this file, see
https://docs.djangoproject.com/en/2.2/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/2.2/ref/settings/
"""

import os
import logging #, logging.config
import sys
# from django.utils.log import DEFAULT_LOGGING

# import sentry_sdk
# from sentry_sdk.integrations.django import DjangoIntegration
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
#sys.path.append('/mnt/d/work/python/my_pass/reis/')

# sentry_sdk.init(
#     dsn="https://22e558e0cb164536a1b4c1a72b5b48d6@sentry.io/1486601",
#     integrations=[DjangoIntegration()]
# )

# import sentry_sdk
# from sentry_sdk.integrations.django import DjangoIntegration
# sentry_sdk.init(
#     dsn="https://22e558e0cb164536a1b4c1a72b5b48d6@sentry.io/1486601",
#     integrations=[DjangoIntegration()]
# )

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
# BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/2.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '%8d_9e$6w(aaen$esq7k02kv0=5047d_-3^f@5p-k6e%)k%5tc'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ['.ngrok.io', '127.0.0.1', '0.0.0.0', 'localhost']
print("local settings")


# Database
# https://docs.djangoproject.com/en/2.2/ref/settings/#databases

DATABASES = {
    # 'default': {
    #     'ENGINE': 'django.db.backends.postgresql_psycopg2',
    #     'NAME': 'db_passport',
    #     'HOST': '0.0.0.0',
    #     'USER': 'postgres',
    #     'PASSWORD': 'postgres',
    #     'PORT': '5432',
    #     'ATOMIC_REQUESTS': True,
    # }
    # 'default': {
    #     'ENGINE': 'django.db.backends.postgresql',
    #     'NAME': 'postgres',
    #     'USER': 'postgres',
    #     'HOST': 'postgres-compose',
    #     'PORT': 5432,
    # }

    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'xgb_dbreis',
        'USER': 'postgres',
        'PASSWORD': 'root',
        'HOST': 'localhost',
        'PORT': 5433,
    }

    # 'default': {
    #     'ENGINE': 'django.db.backends.postgresql_psycopg2',
    #     'NAME': 'xgb_dbreis',
    #     'HOST': 'postgres72.1gb.ru',
    #     'USER': 'xgb_dbreis',
    #     'PASSWORD': 'ae554776789',
    #     'PORT': '5432',
    #     'ATOMIC_REQUESTS': True,
    # }
}



##================LOGGING================================
# LOGGING_CONFIG = None
#
# LOGLEVEL = os.environ.get('LOGLEVEL', 'info').upper()
#
# logging.config.dictConfig({
#     'version': 1,
#     'disable_existing_loggers': False,
#     'formatters': {
#         'default': {
#             # exact format is not important, this is the minimum information
#             'format': '%(asctime)s %(name)-12s %(levelname)-8s %(message)s',
#         },
#         'django.server': DEFAULT_LOGGING['formatters']['django.server'],
#     },
#     'handlers': {
#         # console logs to stderr
#         'console': {
#             'class': 'logging.StreamHandler',
#             'formatter': 'default',
#         },
#         # Add Handler for Sentry for `warning` and above
#         'sentry': {
#             'level': 'WARNING',
#             'class': 'raven.contrib.django.raven_compat.handlers.SentryHandler',
#         },
#         'django.server': DEFAULT_LOGGING['handlers']['django.server'],
#     },
#     'loggers': {
#         # default for all undefined Python modules
#         '': {
#             'level': 'WARNING',
#             'handlers': ['console', 'sentry'],
#         },
#         # Our application code
#         'passport_app': {
#             'level': LOGLEVEL,
#             'handlers': ['console', 'sentry'],
#             # Avoid double logging because of root logger
#             'propagate': False,
#         },
#         # Prevent noisy modules from logging to Sentry
#         'noisy_module': {
#             'level': 'ERROR',
#             'handlers': ['console'],
#             'propagate': False,
#         },
#         # Default runserver request logging
#         'django.server': DEFAULT_LOGGING['loggers']['django.server'],
#     },
# })

LOGGING = {
        'version': 1,
        'disable_existing_loggers': False,
        'formatters': {
            'default': {
                'format': '[DJANGO] %(levelname)s %(asctime)s %(module)s '
                          '%(name)s.%(funcName)s:%(lineno)s: %(message)s'
            },
        },
        'handlers': {
            'console': {
                'level': 'DEBUG',
                'class': 'logging.StreamHandler',
                'formatter': 'default',
            }
        },
        'loggers': {
            '*': {
                'handlers': ['console'],
                'level': 'DEBUG',
                'propagate': True,
            }
        },
    }


# Internationalization
# https://docs.djangoproject.com/en/2.2/topics/i18n/


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/2.2/howto/static-files/

STATIC_URL = '/static/'



