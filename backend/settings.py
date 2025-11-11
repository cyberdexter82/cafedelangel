"""
Django settings for backend project.
"""

import os
from pathlib import Path
# 🔥 CRUCIAL para conectar a Azure PostgreSQL
import dj_database_url 

# BASE DIR
# En su estructura, la carpeta de configuración ('backend') está dentro de la carpeta raíz.
BASE_DIR = Path(__file__).resolve().parent.parent

# 🔹 Templates
TEMPLATES_DIR = os.path.join(BASE_DIR, 'templates')


# -----------------------------------------------
# 🔥 CONFIGURACIÓN DE PRODUCCIÓN Y ESTÁTICOS 🔥
# -----------------------------------------------

# 🔹 Archivos estáticos (CSS, JS)
STATIC_URL = '/static/'

STATICFILES_DIRS = [
    os.path.join(BASE_DIR, 'static'),
]

# ESTO RESUELVE EL ERROR 'ImproperlyConfigured'
STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles') 


# SECURITY
SECRET_KEY = 'django-insecure-&+7ia!=_s&c!h8&7j$xh74)c^o(u9=!d5rob2f&%ciux=(z-2)'

# 🔥 DESACTIVADO para producción en Azure
DEBUG = False 

# 🔥 Permitir acceso desde el dominio de Azure
ALLOWED_HOSTS = ['.azurewebsites.net', '127.0.0.1'] 


# 🔹 APLICACIONES
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    # Necesario para manejar dominios, aunque se use poco.
    'django.contrib.sites', 
    'api',
    'usuarios',
]
SITE_ID = 1 # ID necesario para 'django.contrib.sites'


# MIDDLEWARE (Se deja igual)
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

# 🔹 TEMPLATES (Se deja igual)
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
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'backend.wsgi.application'

# 🔥 CONEXIÓN A POSTGRESQL EN AZURE
DATABASES = {
    'default': dj_database_url.config(
        # Lee la cadena de conexión 'DATABASE_URL' que configuró en Azure App Service
        default=os.environ.get('DATABASE_URL')
    )
}

# 🔹 Validadores de contraseña (Se dejan igual)
AUTH_PASSWORD_VALIDATORS = [
    {'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator'},
    {'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator'},
    {'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator'},
    {'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator'},
]

# 🔹 Idioma y zona horaria (Se dejan igual)
LANGUAGE_CODE = 'es-mx'
TIME_ZONE = 'UTC'
USE_I18N = True
USE_TZ = True

# 🔹 Clave primaria por defecto (Se deja igual)
DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

# 🔹 Modelo de usuario personalizado (Se deja igual)
AUTH_USER_MODEL = 'usuarios.Usuario'
LOGIN_URL = 'login'


# 🔹 Configuración de Archivos Media (Imágenes subidas por usuarios)
MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')