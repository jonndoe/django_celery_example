from .celery import app as celery_app

# Celery app is automatically imported when Django starts:
__all__ = ("celery_app")
