import os
from celery import Celery

env = os.environ.get("ENV") or os.environ.get("ENVIRONMENT") or "development"
if env == "production":
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "core.settings.production")
else:
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "core.settings.development")

app = Celery("core")
app.config_from_object("django.conf:settings", namespace="CELERY")
app.autodiscover_tasks()