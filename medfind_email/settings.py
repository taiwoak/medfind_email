import os
from pathlib import Path
from decouple import config

# Build paths inside the project
BASE_DIR = Path(__file__).resolve().parent.parent

# Load secret key securely
SECRET_KEY = config('SECRET_KEY')

# Debug mode (use False in production!)
DEBUG = True

ALLOWED_HOSTS = [
    config("HOST"),
]

# Installed apps (add your app here)
INSTALLED_APPS = [
    'django.contrib.contenttypes',
    'django.contrib.staticfiles',
    'email_service',
    "corsheaders",
]

MIDDLEWARE = [
    "corsheaders.middleware.CorsMiddleware",
    "django.middleware.common.CommonMiddleware",
]

# URL config
ROOT_URLCONF = 'medfind_email.urls'

# Template rendering
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [],
        },
    },
]

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}

WSGI_APPLICATION = 'medfind_email.wsgi.application'

# Gmail SMTP Email Configuration
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_PORT = 587
EMAIL_USE_TLS = True
EMAIL_HOST_USER = config('EMAIL_HOST_USER')
EMAIL_HOST_PASSWORD = config('EMAIL_HOST_PASSWORD')
DEFAULT_FROM_EMAIL = config('DEFAULT_FROM_EMAIL')

# Useful for rendering URLs or internal service calling

CORS_ALLOWED_ORIGINS = [
    config("FRONTEND_URL"),
    config("FRONTEND_URL_2"),
]

CORS_ALLOW_CREDENTIALS = True

# Static files (optional)
STATIC_URL = '/static/'
