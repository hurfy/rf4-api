from celery        import Celery
from os            import environ

environ.setdefault('DJANGO_SETTINGS_MODULE', f'config.settings.settings')
app = Celery('app')

app.config_from_object(f'django.conf:settings', namespace='CELERY')
app.autodiscover_tasks()