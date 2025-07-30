# Development Log

## 2025-07-30 – Celery configuration now requires explicit environment

- Updated `core/celery.py` to require the `DJANGO_SETTINGS_MODULE` environment variable to be set, instead of defaulting to development settings.
- This change prevents accidental use of development configuration in production or other environments.
- If `DJANGO_SETTINGS_MODULE` is not set, Celery will raise a clear error and refuse to start.
- See `README.md` for details on configuring environment variables and running Celery.

## 2025-07-30 – Django Channels and Real-Time Chat Setup

- Integrated Django Channels for websocket support.
- Added Redis service to both development and production docker-compose files for channel layers.
- Updated `core/settings/base.py` for Channels configuration.
- Updated `core/asgi.py` to use ProtocolTypeRouter and websocket routing.
- Created `core/routing.py`, `apps/chats/routing.py`, and `apps/chats/consumers.py` for websocket chat.
- See [`docs/2025-07-30-django-channels-chat.md`](2025-07-30-django-channels-chat.md) for full details and plan.
---
This log tracks architectural decisions and significant changes. For task-specific details, see individual task files in `/docs`.