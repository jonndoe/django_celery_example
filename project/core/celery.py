import os

from celery import Celery

# Celery knows how to find the Django project
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "core.settings")

# Created Celery instance with name="core"
app = Celery("core")

# Loaded celery configuration values, prefix CELERY_ to be added
app.config_from_object("django.conf:settings", namespace="CELERY")

# Celery looks up for tasks in all apps defined in INSTALLED_APPS
app.autodiscover_tasks()