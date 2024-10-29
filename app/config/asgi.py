from django.core.asgi import get_asgi_application

from os               import environ

# Setup wsgi application
environ.setdefault("DJANGO_SETTINGS_MODULE", "config.settings.settings")
application = get_asgi_application()
