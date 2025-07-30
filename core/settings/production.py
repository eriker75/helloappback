from .base import *
import os

DEBUG = os.environ.get('DJANGO_DEBUG', 'False') == 'True'
ALLOWED_HOSTS = os.environ.get('DJANGO_ALLOWED_HOSTS', '').split(',')

DATABASES = {
    'default': {
        'ENGINE': os.environ.get('DJANGO_DB_ENGINE', 'django.db.backends.postgresql'),
        'NAME': os.environ.get('DJANGO_DB_NAME', ''),
        'USER': os.environ.get('DJANGO_DB_USER', ''),
        'PASSWORD': os.environ.get('DJANGO_DB_PASSWORD', ''),
        'HOST': os.environ.get('DJANGO_DB_HOST', ''),
        'PORT': os.environ.get('DJANGO_DB_PORT', '5432'),
    }
}

STATIC_URL = os.environ.get('DJANGO_STATIC_URL', '/static/')
STATIC_ROOT = os.environ.get('DJANGO_STATIC_ROOT', os.path.join(BASE_DIR, 'staticfiles'))
MEDIA_URL = os.environ.get('DJANGO_MEDIA_URL', '/media/')
MEDIA_ROOT = os.environ.get('DJANGO_MEDIA_ROOT', os.path.join(BASE_DIR, 'media'))

SECURE_SSL_REDIRECT = True
SESSION_COOKIE_SECURE = True
CSRF_COOKIE_SECURE = True
SECURE_HSTS_SECONDS = 3600
SECURE_HSTS_INCLUDE_SUBDOMAINS = True
SECURE_HSTS_PRELOAD = True