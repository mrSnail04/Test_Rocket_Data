from celery import Celery
from .models import Employee

app = Celery('Test_Rocket', broker='redis://redis:6379/0')


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
    id_employee_update = []
    for id_empl in id_employee:
        id_em = Employee.objects.get(id=id_empl)
        id_em.total_paid = 0
        id_employee_update.append(id_em)
    Employee.objects.bulk_update(id_employee_update, ["total_paid"])
    return
