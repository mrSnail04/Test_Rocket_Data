from celery import shared_task
from celery import Celery
from .models import *
app = Celery('Test_Rocket', broker='redis://127.0.0.1:6379/0')


@app.task
def sum_salary():
    list_id = Employee.objects.all().values_list('id', flat=True)
    for id_employee in list_id:
        user = Employee.objects.get(id=id_employee)
        user.total_paid += user.salary
        user.save()


@app.task
def clear_total_paid_task(modeladmin, request, queryset):
    queryset.update(total_paid=f"{0}")
    return

