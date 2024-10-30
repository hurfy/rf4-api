from pathlib      import Path

from config.setup import DJANGO_KEY, PG_ADDRESS, PG_NAME, PG_PASSWORD, PG_PORT, PG_USERNAME

BASE_DIR = Path(__file__).resolve().parent.parent.parent

# Django app
SECRET_KEY    = DJANGO_KEY
ALLOWED_HOSTS = []
DEBUG         = True

# Application definition
INSTALLED_APPS = [
    # Django
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    # Api
    "apps.core",
    "apps.api",
    "apps.parser",
    # Libs
    "rest_framework",
    "django_filters",
    "drf_spectacular",
]

MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
]

ROOT_URLCONF = "config.urls"

TEMPLATES = [
    {
        "BACKEND" : "django.template.backends.django.DjangoTemplates",
        "DIRS"    : [],
        "APP_DIRS": True,
        "OPTIONS" : {
            "context_processors": [
                "django.template.context_processors.debug",
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
            ],
        },
    },
]

WSGI_APPLICATION = "config.wsgi.application"

# Database
DATABASES = {
    "default": {
        "ENGINE"  : "django.db.backends.postgresql_psycopg2",
        "NAME"    : PG_NAME,
        "USER"    : PG_USERNAME,
        "PASSWORD": PG_PASSWORD,
        "HOST"    : PG_ADDRESS,
        "PORT"    : PG_PORT,
        "OPTIONS" : {
            "client_encoding": "UTF8",
        },
    }
}

# Password validation
AUTH_PASSWORD_VALIDATORS = [
    {
        "NAME": "django.contrib.auth.password_validation.UserAttributeSimilarityValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.MinimumLengthValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.CommonPasswordValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.NumericPasswordValidator",
    },
]

# Internationalization
LANGUAGE_CODE = "en-us"
TIME_ZONE     = "UTC"
USE_I18N      = True
USE_TZ        = True

# Static files (CSS, JavaScript, Images)
STATIC_URL = "static/"

# Default primary key field type
DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"

# Parser
PARSER_REGION = "ru"  # com, ru, pl, de, jp, kr, fr, cn

# REST Framework
REST_FRAMEWORK = {
    # Pagination
    "DEFAULT_PAGINATION_CLASS": "rest_framework.pagination.LimitOffsetPagination",
    "PAGE_SIZE"               : 30,
    # Render
    "DEFAULT_RENDERER_CLASSES": [
        "rest_framework.renderers.JSONRenderer",
    ],
    # Filters
    "DEFAULT_FILTER_BACKENDS" : [
            "django_filters.rest_framework.DjangoFilterBackend",
            "rest_framework.filters.OrderingFilter",
    ],
    # Open API
    "DEFAULT_SCHEMA_CLASS"    : "drf_spectacular.openapi.AutoSchema",
}

# OpenAPI
SPECTACULAR_SETTINGS = {
    "TITLE"               : "Russian Fishing 4 - Community API",
    "DESCRIPTION"         : "Soon.TM",
    "VERSION"             : "1.0.0",
    "SERVE_INCLUDE_SCHEMA": False,
    "SERVERS"             : [
        {"url": "https://api.rf4.com/v1"},
    ],
}

# Celery
CELERY_BROKER_URL                         = f"redis://127.0.0.1:6379/0"
CELERY_BROKER_CONNECTION_RETRY_ON_STARTUP = True