from celery import shared_task
from .models import *

@shared_task
def sum_salary():
    list_id = Employee.objects.all().values_list('id', flat=True)
    for id_employee in list_id:
        user = Employee.objects.get(id=id_employee)
        user.total_paid += user.salary
        print(user.total_paid)
        user.save()


