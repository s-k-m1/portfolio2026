import os
import dj_database_url
from .base import *

DEBUG = False

ALLOWED_HOSTS = [
    "portfolio2026-buti.onrender.com",
    "saroj01.com.np",
]

DATABASES = {
    "default": dj_database_url.config(
        default=os.getenv("DATABASE_URL"),
        conn_max_age=600,
        ssl_require=True
    )
}

SECURE_SSL_REDIRECT = True
SESSION_COOKIE_SECURE = True
CSRF_COOKIE_SECURE = True

STATIC_URL = "/static/"
STATIC_ROOT = BASE_DIR / "staticfiles"

CSRF_TRUSTED_ORIGINS = [
    "https://portfolio2026-buti.onrender.com",
    "https://saroj01.com.np",
]

CSRF_TRUSTED_ORIGINS = [
    "https://portfolio2026-buti.onrender.com",
    "https://saroj01.com.np",
]

SECURE_PROXY_SSL_HEADER = ("HTTP_X_FORWARDED_PROTO", "https")