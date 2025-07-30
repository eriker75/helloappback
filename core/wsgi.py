import os

from django.core.wsgi import get_wsgi_application

env = os.environ.get("ENV") or os.environ.get("ENVIRONMENT") or "development"
if env == "production":
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "core.settings.production")
else:
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "core.settings.development")

application = get_wsgi_application()
