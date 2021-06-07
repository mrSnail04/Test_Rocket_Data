from celery import shared_task
from Test_Rocket.celery import app
from .models import *


@shared_task
def sum_salary():
    list_id = Employee.objects.all().values_list('id', flat=True)
    for id_employee in list_id:
        user = Employee.objects.get(id=id_employee)
        user.total_paid += user.salary
        user.save()


@task
def clear_total_paid_task(modeladmin, request, queriset):
    queriset.update(total_paid=f'{0}')

