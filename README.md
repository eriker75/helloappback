# HelloBack Project

This project is a Django-based backend with Celery integration for asynchronous task processing.

## Environment Configuration

**Important:**  
You must set the `DJANGO_SETTINGS_MODULE` environment variable before running Django or Celery.  
- For development:  
  `export DJANGO_SETTINGS_MODULE=core.settings.development`
- For production:  
  `export DJANGO_SETTINGS_MODULE=core.settings.production`

If this variable is not set, Celery will refuse to start and raise an error.

## Running Celery

To start the Celery worker:
```bash
celery -A core worker --loglevel=info
```
Make sure the correct environment variables are set.

## Documentation

- See [`docs/devlog.md`](docs/devlog.md) for a log of architectural decisions and significant changes.
- Task-specific documentation can be found in `/docs`.

---
*Keep this README updated with any changes to environment or configuration requirements.*