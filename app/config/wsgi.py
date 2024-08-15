from django.core.wsgi import get_wsgi_application

from os               import environ

# Setup wsgi application
environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings.settings')
application = get_wsgi_application()
