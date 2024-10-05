import os
from pathlib import Path

import environ
from corsheaders.defaults import default_headers

env = environ.Env(DEBUG=(bool, False))

BASE_DIR = Path(__file__).resolve().parent.parent

environ.Env.read_env(os.path.join(BASE_DIR, ".env.dev"))

DEBUG = env.bool("DJANGO_DEBUG", default=True)
SECRET_KEY = env("DJANGO_SECRET_KEY", default="django-strong-key")

ALLOWED_HOSTS = ["*"] if DEBUG else env("ALLOWED_HOSTS").split(" ")

DOMAIN_NAME = env("BACKEND_DOMAIN")
CLIENT_DOMAIN = env("CLIENT_DOMAIN")

INSTALLED_APPS = [
    "corsheaders",
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    "django.contrib.postgres",
    "django_redis",
    "django_prometheus",
    "rest_framework",
    "django_filters",
    "debug_toolbar",
    "redisboard",
    "drf_spectacular",
    "graphene_django",
    "core",
    "patient",
    "employee",
    "business",
    "schemas",
]

MIDDLEWARE = [
    "django_prometheus.middleware.PrometheusBeforeMiddleware",
    "corsheaders.middleware.CorsMiddleware",
    "django.middleware.gzip.GZipMiddleware",
    "debug_toolbar.middleware.DebugToolbarMiddleware",
    "django.middleware.security.SecurityMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
    "django.middleware.locale.LocaleMiddleware",
    "core.middleware.TokenMiddleware",
    "core.middleware.PingUserMiddleware",
    "django_prometheus.middleware.PrometheusAfterMiddleware",
]

ROOT_URLCONF = "config.urls"
WSGI_APPLICATION = "config.wsgi.application"
ASGI_APPLICATION = "config.asgi.application"

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [],
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.debug",
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
            ],
        },
    },
]

REST_FRAMEWORK = {
    "DEFAULT_RENDERER_CLASSES": [
        "rest_framework.renderers.JSONRenderer",
        "rest_framework.renderers.BrowsableAPIRenderer",
    ],
    "DEFAULT_PARSER_CLASSES": ["rest_framework.parsers.JSONParser", "rest_framework.parsers.MultiPartParser"],
    "DEFAULT_AUTHENTICATION_CLASSES": ["core.authentication.SessionTokenAuthentication"],
    "DEFAULT_FILTER_BACKENDS": [
        "django_filters.rest_framework.DjangoFilterBackend",
        "rest_framework.filters.SearchFilter",
        "rest_framework.filters.OrderingFilter",
    ],
    "DEFAULT_THROTTLE_CLASSES": [
        "core.throttling.BurstRateThrottle",
    ],
    "DEFAULT_THROTTLE_RATES": {
        "burst": "20/second",
    },
    "DEFAULT_VERSIONING_CLASS": "rest_framework.versioning.NamespaceVersioning",
    "DEFAULT_SCHEMA_CLASS": "drf_spectacular.openapi.AutoSchema",
    "DEFAULT_PAGINATION_CLASS": "core.paginations.StandardPageNumberPagination",
}

SPECTACULAR_SETTINGS = {
    "TITLE": "Swagger API",
    "DESCRIPTION": "Swagger API description",
    "VERSION": "1.0.0",
    "SERVE_INCLUDE_SCHEMA": False,
}

GRAPHENE = {"SCHEMA": "config.schema.schema"}

DATABASE_ENGINE = env("DATABASE_ENGINE", default="django.db.backends.sqlite3")

if DATABASE_ENGINE == "django.db.backends.sqlite3":
    DATABASES = {
        "default": {
            "ENGINE": DATABASE_ENGINE,
            "NAME": BASE_DIR / "db.sqlite3",
        }
    }
else:
    DATABASES = {
        "default": {
            "ENGINE": DATABASE_ENGINE,
            "NAME": env("POSTGRES_DB", default=os.path.join(BASE_DIR, "db.sqlite3")),
            "USER": env("POSTGRES_USER", default="postgres"),
            "PASSWORD": env("POSTGRES_PASSWORD", default="root"),
            "HOST": env("POSTGRES_HOST", default="localhost"),
            "PORT": env("POSTGRES_PORT", default="5432"),
            "OPTIONS": {},
        },
    }


AUTH_USER_MODEL = "core.User"

LANGUAGE_CODE = "ru-ru"
TIME_ZONE = "Europe/Moscow"
USE_I18N = True
USE_L10N = True

DJANGO_SUPERUSER_USERNAME = env("DJANGO_SUPERUSER_USERNAME", default="admin")
DJANGO_SUPERUSER_EMAIL = env("DJANGO_SUPERUSER_EMAIL", default="admin@host.com")
DJANGO_SUPERUSER_PHONE = env("DJANGO_SUPERUSER_PHONE", default="+79999999999")
DJANGO_SUPERUSER_PASSWORD = env("DJANGO_SUPERUSER_PASSWORD", default="admin")

SECURE_HSTS_PRELOAD = not DEBUG
SECURE_SSL_REDIRECT = not DEBUG
SECURE_HSTS_INCLUDE_SUBDOMAINS = True
SECURE_HSTS_SECONDS = 0 if DEBUG else 31536000
SECURE_PROXY_SSL_HEADER = ("HTTP_X_FORWARDED_PROTO", "https") if not DEBUG else None

X_FRAME_OPTIONS = "DENY"
SECURE_BROWSER_XSS_FILTER = True
SECURE_CONTENT_TYPE_NOSNIFF = True
SECURE_REFERRER_POLICY = "same-origin"

SESSION_COOKIE_SECURE = True
SESSION_COOKIE_HTTPONLY = True
SESSION_COOKIE_SAMESITE = "Lax"

CSRF_COOKIE_AGE = 31449600
CSRF_COOKIE_SAMESITE = "Lax"
CSRF_COOKIE_NAME = "csrftoken"
CSRF_COOKIE_SECURE = not DEBUG
CSRF_COOKIE_HTTPONLY = not DEBUG
CSRF_HEADER_NAME = "X-CSRFToken"

CORS_ALLOW_ALL_ORIGINS = False
CORS_ALLOW_CREDENTIALS = True
CORS_ORIGIN_ALLOW_ALL = False
CORS_ORIGIN_WHITELIST = env("ALLOWED_HOSTS").split(" ")
CSRF_TRUSTED_ORIGINS = env("ALLOWED_HOSTS").split(" ")
CORS_EXPOSE_HEADERS = ["Content-Type", "X-CSRFToken"]
CORS_ALLOW_METHODS = ["DELETE", "GET", "OPTIONS", "PATCH", "POST", "PUT"]
CORS_ALLOW_HEADERS = default_headers + ("http-x-role", "Content-Disposition")

REDIS_HOST = env("REDIS_HOST", default="redis")
REDIS_PORT = env("REDIS_PORT", default=6379)
REDIS_PASSWORD = env("REDIS_PASSWORD", default=None)
REDIS_DB = 0

if REDIS_PASSWORD:
    REDIS_URL = f"redis://:{REDIS_PASSWORD}@{REDIS_HOST}:{REDIS_PORT}/{REDIS_DB}"
else:
    REDIS_URL = f"redis://{REDIS_HOST}:{REDIS_PORT}/{REDIS_DB}"

RABBITMQ_USER = env("RABBITMQ_USER", default="guest")
RABBITMQ_PASSWORD = env("RABBITMQ_DEFAULT_PASS", default="guest")
RABBITMQ_HOST = env("RABBITMQ_HOST", default="rabbitmq")
RABBITMQ_PORT = env("RABBITMQ_PORT", default=5672)
RABBITMQ_VHOST = env("RABBITMQ_VHOST", default="/")

if RABBITMQ_USER and RABBITMQ_PASSWORD:
    RABBITMQ_URL = f"amqp://{RABBITMQ_USER}:{RABBITMQ_PASSWORD}@{RABBITMQ_HOST}:{RABBITMQ_PORT}/{RABBITMQ_VHOST}"
else:
    RABBITMQ_URL = f"amqp://{RABBITMQ_HOST}:{RABBITMQ_PORT}/{RABBITMQ_VHOST}"

CACHES = {
    "default": {
        "BACKEND": "django_redis.cache.RedisCache",
        "LOCATION": REDIS_URL,
        "OPTIONS": {
            "CLIENT_CLASS": "django_redis.client.DefaultClient",
        },
    }
}

CACHE_MIDDLEWARE_ALIAS = "default"
CACHE_MIDDLEWARE_SECONDS = 60 * 15
CACHE_MIDDLEWARE_KEY_PREFIX = "hospital"
CACHE_TTL = 60 * 15

CELERY_BROKER_URL = RABBITMQ_URL
CELERY_RESULT_BACKEND = RABBITMQ_URL
CELERY_ACCEPT_CONTENT = ["application/json"]
CELERY_TASK_SERIALIZER = "json"
CELERY_RESULT_SERIALIZER = "json"
CELERY_TIMEZONE = TIME_ZONE
CELERY_BROKER_CONNECTION_RETRY_ON_STARTUP = True

REQUEST_RATE_LIMIT = 999999
REQUEST_RATE_PERIOD = 999999

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

STATIC_URL = "/static/"
STATICFILES_DIRS = (BASE_DIR / "static",)

MEDIA_URL = "/media/"
MEDIA_ROOT = os.path.join(BASE_DIR, "media")

DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"

if DEBUG:
    EMAIL_BACKEND = "django.core.mail.backends.console.EmailBackend"

HASH_ALGORITHM = env("HASH_ALGORITHM", default="HS256")

SESSION_TIMEOUT = 3600
SESSION_EXPIRE_MINUTES = 60
SESSION_EXPIRE_HOURS = 3
SESSION_EXPIRE_DAYS = 7

YOOKASSA_ACCOUNT_ID = env("YOOKASSA_ACCOUNT_ID", default="")
YOOKASSA_SECRET_KEY = env("YOOKASSA_SECRET_KEY", default="")
YOOKASSA_RETURN_URL = env("YOOKASSA_RETURN_URL", default="")

YOOKASSA_DEBUG = DEBUG

INVOICE_DAYS_TO_EXPIRE = 30
PAYMENT_DAYS_TO_EXPIRE = 1

DECIMAL_PLACES = 2

if DEBUG:
    DEBUG_TOOLBAR_PANELS = [
        "debug_toolbar.panels.history.HistoryPanel",
        "debug_toolbar.panels.versions.VersionsPanel",
        "debug_toolbar.panels.timer.TimerPanel",
        "debug_toolbar.panels.settings.SettingsPanel",
        "debug_toolbar.panels.headers.HeadersPanel",
        "debug_toolbar.panels.request.RequestPanel",
        "debug_toolbar.panels.sql.SQLPanel",
        "debug_toolbar.panels.staticfiles.StaticFilesPanel",
        "debug_toolbar.panels.templates.TemplatesPanel",
        "debug_toolbar.panels.cache.CachePanel",
        "debug_toolbar.panels.signals.SignalsPanel",
        "debug_toolbar.panels.redirects.RedirectsPanel",
        "debug_toolbar.panels.profiling.ProfilingPanel",
    ]
