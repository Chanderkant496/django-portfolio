import os
from pathlib import Path
import dj_database_url

BASE_DIR = Path(__file__).resolve().parent.parent

# ------------ SECURITY SETTINGS ------------
SECRET_KEY = os.environ.get("SECRET_KEY", "django-insecure-local-key-for-testing-only")

DEBUG = False

# IMPORTANT: Allow Render domai
ALLOWED_HOSTS = [
    'localhost',
    '127.0.0.1',
    '.onrender.com'
]




# ------------ INSTALLED APPS ------------
INSTALLED_APPS = [
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",

    "base",   # your Django app
]


# ------------ MIDDLEWARE ------------
MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "whitenoise.middleware.WhiteNoiseMiddleware",  # Static files for Render
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
]


# ------------ URL / WSGI ------------
ROOT_URLCONF = "portfolio.urls"
WSGI_APPLICATION = "portfolio.wsgi.application"


# ------------ DATABASE SETTINGS (Render Uses PostgreSQL) ------------
DATABASES = {
    "default": dj_database_url.config(
        default="sqlite:///" + str(BASE_DIR / "db.sqlite3"),  # Local fallback
        conn_max_age=600,
    )
}


# ------------ TEMPLATES ------------
TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [BASE_DIR / "templates"],  # Global templates folder
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


# ------------ STATIC FILES (Render Requires This) ------------
STATIC_URL = "/static/"
STATIC_ROOT = BASE_DIR / "staticfiles"      # Render will collect static here
STATICFILES_DIRS = [BASE_DIR / "static"]    # Your static folder

STATICFILES_STORAGE = "whitenoise.storage.CompressedManifestStaticFilesStorage"


# ------------ DEFAULT AUTO FIELD ------------
DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"
