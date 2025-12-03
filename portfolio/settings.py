import os
from pathlib import Path
import dj_database_url

BASE_DIR = Path(__file__).resolve().parent.parent

# -------- SECURITY SETTINGS --------
SECRET_KEY = "django-insecure-local-key-for-testing-only"
DEBUG = True
ALLOWED_HOSTS = ["localhost", "127.0.0.1"]  # ✅ sirf local ke liye

# -------- INSTALLED APPS --------
INSTALLED_APPS = [
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",

    "base",  # ✅ ye aapka Django app folder hai (module)
]

# -------- DATABASE SETTINGS --------
DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.sqlite3",
        "NAME": BASE_DIR / "db.sqlite3",
    }
}

# -------- MIDDLEWARE SETTINGS --------
MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
]

# -------- URL & WSGI --------
ROOT_URLCONF = "portfolio.urls"
WSGI_APPLICATION = "portfolio.wsgi.application"

# -------- TEMPLATES SETTINGS --------
TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [BASE_DIR / "templates"],  # ✅ agar templates folder ho
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

# -------- STATIC FILE SETTINGS --------
STATIC_URL = "/static/"
STATIC_ROOT = BASE_DIR / "staticfiles"  # local me use nahi hota but path set ✅
STATICFILES_DIRS = [BASE_DIR / "static"]  # ✅ aapka static folder

# -------- DEFAULT AUTO FIELD --------
DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"
