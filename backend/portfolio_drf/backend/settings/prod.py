import os
import dj_database_url
from pathlib import Path
from .base import * # --- 1. ENVIRONMENT DETECTION ---
# Render automatically sets RENDER=true. 
# This helps us avoid "fcntl" errors and HTTPS loops on your local Windows PC.
IS_RENDER = os.environ.get("RENDER", "False").lower() == "true"

# --- 2. CORE SECURITY ---
SECRET_KEY = os.environ.get("SECRET_KEY")
DEBUG = os.environ.get("DEBUG", "False").lower() == "true"

# --- 3. THE PERMANENT 400 FIX (ALLOWED_HOSTS) ---
# .strip() removes spaces; if host.strip() removes empty commas.
raw_hosts = os.environ.get("ALLOWED_HOSTS", "")
ALLOWED_HOSTS = [host.strip() for host in raw_hosts.split(",") if host.strip()]

# --- 4. RENDER-SPECIFIC PROXY & SSL ---
if IS_RENDER:
    # Tells Django it's behind Render's HTTPS proxy
    SECURE_PROXY_SSL_HEADER = ("HTTP_X_FORWARDED_PROTO", "https")
    SECURE_SSL_REDIRECT = True
    SESSION_COOKIE_SECURE = True
    CSRF_COOKIE_SECURE = True
    
    # Clean CSRF origins list
    raw_csrf = os.environ.get("CSRF_TRUSTED_ORIGINS", "")
    CSRF_TRUSTED_ORIGINS = [o.strip() for o in raw_csrf.split(",") if o.strip()]
else:
    # Safe defaults for local Windows testing
    ALLOWED_HOSTS = ["127.0.0.1", "localhost"]
    SECURE_SSL_REDIRECT = False

# --- 5. DATABASE SETUP ---
DATABASES = {
    "default": dj_database_url.config(
        default=os.environ.get("DATABASE_URL"),
        conn_max_age=600,
        ssl_require=IS_RENDER # Only require SSL on Render
    )
}

# --- 6. STATIC FILES (WhiteNoise) ---
STATIC_URL = "/static/"
STATIC_ROOT = BASE_DIR / "staticfiles"
# manifest storage keeps files versioned (prevents caching issues)
STATICFILES_STORAGE = "whitenoise.storage.CompressedManifestStaticFilesStorage"