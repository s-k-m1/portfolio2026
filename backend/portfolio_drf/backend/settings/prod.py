import os
import dj_database_url
from pathlib import Path
from .base import *

# 1. SECURITY & DEBUG
SECRET_KEY = os.environ.get("SECRET_KEY")
DEBUG = os.environ.get("DEBUG", "False").lower() == "true"

# 2. NETWORKING & HOSTS
raw_hosts = os.environ.get("ALLOWED_HOSTS", "")
ALLOWED_HOSTS = [host.strip() for host in raw_hosts.split(",") if host.strip()]

RENDER_EXTERNAL_HOSTNAME = os.environ.get('RENDER_EXTERNAL_HOSTNAME')
if RENDER_EXTERNAL_HOSTNAME:
    ALLOWED_HOSTS.append(RENDER_EXTERNAL_HOSTNAME)

if not ALLOWED_HOSTS:
    ALLOWED_HOSTS = ['*']

# 3. MIDDLEWARE (Ensuring WhiteNoise is in the correct spot)
if 'whitenoise.middleware.WhiteNoiseMiddleware' not in MIDDLEWARE:
    MIDDLEWARE.insert(1, 'whitenoise.middleware.WhiteNoiseMiddleware')

# 4. DATABASE (Production PostgreSQL)
DATABASES = {
    "default": dj_database_url.config(
        default=os.environ.get("DATABASE_URL"),
        conn_max_age=600,
        ssl_require=True
    )
}

# 5. STATIC FILES (WhiteNoise Fix)
STATIC_URL = "/static/"
STATIC_ROOT = BASE_DIR / "staticfiles"

# Use CompressedStaticFilesStorage to avoid 'Missing File' errors during deployment
STATICFILES_STORAGE = "whitenoise.storage.CompressedStaticFilesStorage"

# 6. HTTPS SETTINGS
if not DEBUG:
    SECURE_PROXY_SSL_HEADER = ("HTTP_X_FORWARDED_PROTO", "https")
    SECURE_SSL_REDIRECT = True
    SESSION_COOKIE_SECURE = True
    CSRF_COOKIE_SECURE = True
    
    raw_csrf = os.environ.get("CSRF_TRUSTED_ORIGINS", "")
    CSRF_TRUSTED_ORIGINS = [o.strip() for o in raw_csrf.split(",") if o.strip()]
    
    if RENDER_EXTERNAL_HOSTNAME:
        CSRF_TRUSTED_ORIGINS.append(f"https://{RENDER_EXTERNAL_HOSTNAME}")