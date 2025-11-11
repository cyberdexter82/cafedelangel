"""
Django settings for backend project.
"""

import os
from pathlib import Path

# BASE DIR
BASE_DIR = Path(__file__).resolve().parent.parent

# 🔹 Templates
TEMPLATES_DIR = os.path.join(BASE_DIR, 'templates')

# 🔹 Archivos estáticos (CSS, JS, imágenes)
STATIC_URL = '/static/'
STATICFILES_DIRS = [
    os.path.join(BASE_DIR, 'static'),
]

# SECURITY
SECRET_KEY = 'django-insecure-&+7ia!=_s&c!h8&7j$xh74)c^o(u9=!d5rob2f&%ciux=(z-2)'
DEBUG = True
ALLOWED_HOSTS = []

# APLICACIONES
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'api',
    'usuarios',
]

# MIDDLEWARE
MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'backend.urls'

# 🔹 TEMPLATES
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [TEMPLATES_DIR],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                # --- 👇 ¡ESTA ES LA LÍNEA CORREGIDA! 👇 ---
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'backend.wsgi.application'

# 🔹 BASE DE DATOS (por ahora SQLite)
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}

# 🔹 Validadores de contraseña
AUTH_PASSWORD_VALIDATORS = [
    {'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator'},
    {'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator'},
    {'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator'},
    {'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator'},
]

# 🔹 Idioma y zona horaria
LANGUAGE_CODE = 'es-mx'
TIME_ZONE = 'UTC'
USE_I18N = True
USE_TZ = True

# 🔹 Clave primaria por defecto
DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

# 🔹 Modelo de usuario personalizado
AUTH_USER_MODEL = 'usuarios.Usuario'

# --- 👇 Esta línea está perfecta 👇 ---
LOGIN_URL = 'login'


# --- 👇 ¡LÍNEAS AÑADIDAS PARA LAS IMÁGENES DE PRODUCTOS! 👇 ---

# --- Configuración de Archivos Media (Imágenes subidas por usuarios) ---

# La URL base para los archivos media (ej: /media/productos/cafe.png)
MEDIA_URL = '/media/'

# La ruta en tu PC donde se guardarán esas imágenes
# Creará una carpeta 'media' en la raíz de tu proyecto
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')