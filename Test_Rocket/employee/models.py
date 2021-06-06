from django.db import models


class Employee(models.Model):
    LEVEL = [
        ('Level_1', 'Первый уровень'),
        ('Level_2', 'Второй уровень'),
        ('Level_3', 'Третий уровень'),
        ('Level_4', 'Четвёртый уровень'),
        ('Level_5', 'Пятый уровень'),
    ]

    first_name = models.CharField(max_length=25, verbose_name='Имя')
    last_name = models.CharField(max_length=25, verbose_name='Фамилия')
    second_name = models.CharField(max_length=25, verbose_name='Отчество', blank=True, null=True)
    position = models.ForeignKey('Position', on_delete=models.PROTECT, verbose_name='Должность', default=1)
    date_of_employment = models.DateField(verbose_name='Дата приёма на работу')
    salary = models.DecimalField(max_digits=10, decimal_places=2, verbose_name='Заработная плата')
    total_paid = models.DecimalField(max_digits=10, decimal_places=2, verbose_name='Всего заплатили')
    chief = models.ForeignKey('Employee', on_delete=models.PROTECT, blank=True, null=True, verbose_name='Начальник')
    level = models.CharField(max_length=20, choices=LEVEL, verbose_name='Уровень', null=True)

    class Meta:
        verbose_name_plural = 'Сотрудники'
        verbose_name = 'Сотрудник'

    def __str__(self):
        return self.first_name + ' ' + self.last_name


class Position(models.Model):
    name = models.CharField(max_length=100, verbose_name='Должность')

    def __str__(self):
        return self.name

