import os

from celery import Celery

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "django_course.settings")

celery_app = Celery("braniac", broker='redis://127.0.0.1:6379')
celery_app.config_from_object("django.conf:settings", namespace="CELERY")
celery_app.autodiscover_tasks()
