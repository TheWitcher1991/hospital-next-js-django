from django.db import models
from employee import Employee


class Position(models.Model):
    name = models.CharField('Название', max_length=256)
    functions = models.TextField('Функции')
    salary = models.DecimalField('Зарплата', max_digits=10, decimal_places=0)

    def __str__(self):
        return f'{self.name} | {self.salary} руб.'

    class Meta:
        verbose_name = 'Должность'
        verbose_name_plural = 'Должности'


class Cabinet(models.Model):
    name = models.CharField('Название', max_length=256)
    number = models.CharField('Номер', max_length=10)

    def __str__(self):
        return f'{self.name} | {self.number}'

    class Meta:
        verbose_name = 'Кабинет'
        verbose_name_plural = 'Кабинеты'


class Shift(models.Model):
    number = models.CharField('Номер смены', max_length=10)
    start = models.TimeField('Старт смены')
    end = models.TimeField('Конец смены')

    def __str__(self):
        return f'{self.number} | {self.start} - {self.end}'

    class Meta:
        verbose_name = 'Смена'
        verbose_name_plural = 'Смены'


class Schedule(models.Model):
    date = models.DateField('Дата графика работы')
    shift = models.ForeignKey(to=Shift, on_delete=models.CASCADE)
    employee = models.ForeignKey(to=Employee, on_delete=models.CASCADE)

    class Meta:
        verbose_name = 'График работы'
        verbose_name_plural = 'График работы'


