"""Запустить python fake.py что бы добавить донные о сотрудниках
 populate(n) n-сколько сотрудников добавить.
 Если в БД нету ни одного сотрудника, то в начале добавится сотрудник Maksim Bulavsky, а потом остальные.
 """
import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'Test_Rocket.settings')
django.setup()

from random import randint, choice
import random
from employee.models import Employee, Position
from faker import Faker

fake = Faker()
level = []
for number_tuple_level in range(len(Employee.LEVEL)):
    level.append(Employee.LEVEL[number_tuple_level][0])

position = Position.objects.all().values_list('id', flat=True)

""" Функция по заполнению таблицы сотрудников при помощи Faker """


def populate(N=5):
    if len(Employee.objects.all().values_list('id', flat=True)) == 0:
        Employee.objects.get_or_create(first_name='Maksim',
                                       last_name='Bulavsky',
                                       second_name='Andreevich',
                                       date_of_employment='2021-06-06',
                                       salary=900,
                                       total_paid=5000,
                                       level='Level_1',
                                       position_id=1,
                                       chief_id=None,
                                       )

    for entry in range(N):
        fake_first_name = fake.first_name()
        fake_last_name = fake.last_name()
        fake_second_name = fake.first_name()
        fake_salary = randint(100, 1000)
        fake_total_paid = randint(10000, 50000)
        fake_level = random.choice(level)
        fake_data_of_employment = fake.date_between_dates()
        fake_positional_id = random.choice(position)
        fake_chef_id = random.choice(Employee.objects.all().values_list('id', flat=True))

        employee = Employee.objects.get_or_create(first_name=fake_first_name,
                                                  last_name=fake_last_name,
                                                  second_name=fake_second_name,
                                                  date_of_employment=fake_data_of_employment,
                                                  salary=fake_salary,
                                                  total_paid=fake_total_paid,
                                                  level=fake_level,
                                                  position_id=fake_positional_id,
                                                  chief_id=fake_chef_id,
                                                  )


if __name__ == '__main__':
    print("Populating the databases...Please Wait")
    populate(2)
    print('Populating Complete')

