import os
import dj_database_url
from pathlib import Path
from .base import *

# 1. DETECT ENVIRONMENT
IS_RENDER = os.environ.get("RENDER", "False").lower() == "true"

# 2. CORE SECURITY
SECRET_KEY = os.environ.get("SECRET_KEY")
DEBUG = os.environ.get("DEBUG", "False").lower() == "true"

# 3. PERMANENT 400 FIX
# This cleans up the string from Render's dashboard automatically
raw_hosts = os.environ.get("ALLOWED_HOSTS", "")
if IS_RENDER:
    ALLOWED_HOSTS = [host.strip() for host in raw_hosts.split(",") if host.strip()]
    
    # Tells Django to trust Render's HTTPS proxy
    SECURE_PROXY_SSL_HEADER = ("HTTP_X_FORWARDED_PROTO", "https")
    SECURE_SSL_REDIRECT = True
    SESSION_COOKIE_SECURE = True
    CSRF_COOKIE_SECURE = True
    
    # CSRF Trusted Origins (Must include https://)
    raw_csrf = os.environ.get("CSRF_TRUSTED_ORIGINS", "")
    CSRF_TRUSTED_ORIGINS = [o.strip() for o in raw_csrf.split(",") if o.strip()]
else:
    ALLOWED_HOSTS = ["127.0.0.1", "localhost"]
    SECURE_SSL_REDIRECT = False

# 4. DATABASE
DATABASES = {
    "default": dj_database_url.config(
        default=os.environ.get("DATABASE_URL"),
        conn_max_age=600,
        ssl_require=IS_RENDER
    )
}

# 5. STATIC FILES (WhiteNoise)
STATIC_URL = "/static/"
STATIC_ROOT = BASE_DIR / "staticfiles"
STATICFILES_STORAGE = "whitenoise.storage.CompressedManifestStaticFilesStorage"