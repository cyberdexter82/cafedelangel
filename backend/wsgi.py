import os
from django.core.wsgi import get_wsgi_application

# Importar WhiteNoise AQUI, después de la aplicación
from whitenoise import WhiteNoise

# La importación de settings debe estar dentro de una función si se usa en wsgi
# Usaremos settings.STATIC_ROOT directamente en la envoltura

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'backend.settings')

# 1. Obtiene la aplicación Django estándar
application = get_wsgi_application()

# 2. Envuelve la aplicación con WhiteNoise, usando la configuración global
# Usamos el path completo '/home/site/wwwroot/staticfiles/' como backup absoluto.
application = WhiteNoise(application, root='/home/site/wwwroot/staticfiles/')