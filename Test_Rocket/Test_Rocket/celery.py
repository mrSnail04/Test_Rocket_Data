import os

from celery import Celery

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'Test_Rocket.settings')

app = Celery('Test_Rocket')

app.config_from_object('django.conf:settings', namespace='CELERY')

app.autodiscover_tasks()

app.conf.beat_schedule = {
    'sum_salary': {
        'task': 'employee.tasks.sum_salary',
        'schedule': 7200.0,
    }
}