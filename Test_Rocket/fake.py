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
    tuple_level = Employee.LEVEL[number_tuple_level]
    level.append(tuple_level[0])

position = []
employee_position_all = Position.objects.all().values_list('id', flat=True)
for name_position in employee_position_all:
    position.append(name_position)


def populate(N=5):
    for entry in range(N):
        fake_first_name = fake.first_name()
        fake_last_name = fake.last_name()
        fake_second_name = fake.first_name()
        fake_salary = randint(100, 1000)
        fake_total_paid = randint(10000, 50000)
        fake_level = random.choice(level)
        fake_data_of_employment = fake.date_between_dates()
        fake_positional_id = random.choice(position)

        employee = Employee.objects.get_or_create(first_name=fake_first_name,
                                                  last_name=fake_last_name,
                                                  second_name=fake_second_name,
                                                  date_of_employment=fake_data_of_employment,
                                                  salary=fake_salary,
                                                  total_paid=fake_total_paid,
                                                  level=fake_level,
                                                  position_id=fake_positional_id,
                                                  )


if __name__ == '__main__':
    print("Populating the databases...Please Wait")
    populate(10)
    print('Populating Complete')