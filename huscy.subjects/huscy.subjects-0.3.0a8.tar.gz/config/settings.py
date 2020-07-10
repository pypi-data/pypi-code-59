import os


BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

SECRET_KEY = ')zn(^y3s&=_b7r6+n-grwxnz(lu1mh@k+4tvopv@dawv%a-@1f'

DEBUG = True


# Application definition
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    'django_countries',
    'phonenumber_field',
    'rest_framework',
    'rest_framework_nested',

    'huscy.subjects',
]

# check if django extensions is installed because it's just an extras_require dependency
try:
    import django_extensions
    INSTALLED_APPS.append('django_extensions')
except ImportError:
    pass


MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'config.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
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


# Database
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}


# Internationalization
USE_L10N = True


# Static files (CSS, JavaScript, Images)
STATIC_URL = '/static/'


LOGGING = {
    'version': 1,
    'formatters': {
        'verbose': {
            'format': '{asctime} {module} {message}',
            'style': '{',
        },
    },
    'handlers': {
        'file': {
            'class': 'logging.FileHandler',
            'formatter': 'verbose',
            'filename': '/tmp/subjects_debug.log',
        },
    },
    'loggers': {
        'huscy.subjects': {
            'handlers': ['file'],
            'level': 'INFO',
        },
    },
}
