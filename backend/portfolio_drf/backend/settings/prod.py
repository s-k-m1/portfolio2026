import os
import dj_database_url
from .base import *

DEBUG = False

ALLOWED_HOSTS = [
    host.strip()
    for host in os.getenv(
        "ALLOWED_HOSTS",
        "127.0.0.1,localhost,portfolio2026-buti.onrender.com"
    ).split(",")
    if host.strip()
]

DATABASES = {
    "default": dj_database_url.parse(
        os.getenv("DATABASE_URL"),
        conn_max_age=600
    )
}

SECURE_SSL_REDIRECT = True
SESSION_COOKIE_SECURE = True
CSRF_COOKIE_SECURE = True

STATIC_URL = "/static/"
STATIC_ROOT = BASE_DIR / "staticfiles"

CSRF_TRUSTED_ORIGINS = [
    "https://saroj01.com.np",
    "https://portfolio2026-buti.onrender.com"
]

CORS_ALLOWED_ORIGINS = [
    "https://saroj01.com.np",
    "https://portfolio2026-buti.onrender.com"
]