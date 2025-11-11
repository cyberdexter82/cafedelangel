"""
WSGI config for backend project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/5.2/howto/deployment/wsgi/
"""

import os
from django.core.wsgi import get_wsgi_application
# --- 👇 1. Importa WhiteNoise y settings ---
from whitenoise import WhiteNoise
from django.conf import settings
# ---

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'backend.settings')

# --- 2. Obtiene la aplicación Django estándar ---
application = get_wsgi_application()

# --- 👇 3. Envuelve la aplicación con WhiteNoise ---
# WhiteNoise ahora buscará archivos en la carpeta que definiste en STATIC_ROOT
application = WhiteNoise(application, root=settings.STATIC_ROOT)
# ---