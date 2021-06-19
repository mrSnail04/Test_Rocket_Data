from celery import shared_task
from celery import Celery
from .models import *
app = Celery('Test_Rocket', broker='redis://127.0.0.1:6379/0')


@app.task
def sum_salary():
    update_total_paid = []
    list_id = Employee.objects.all().values_list('id', flat=True)
    list_id = list(list_id)
    for id_employee in list_id:
        user = Employee.objects.get(id=id_employee)
        user.total_paid += user.salary
        update_total_paid.append(user)
    Employee.objects.bulk_update(update_total_paid, ['total_paid'])
    return


@app.task
def clear_total_paid_task(id_employee):
    Employee.objects.filter(id__in=id_employee).update(total_paid=f'{0}')
    return

