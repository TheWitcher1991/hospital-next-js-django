from django.contrib.auth.models import AbstractUser
from django.db import models
from position import Cabinet, Position


class Employee(AbstractUser):
    patronymic = models.CharField('Отчество', max_length=256)
    date = models.DateField('Дата рождения')
    age = models.CharField('Возраст', max_length=10)
    cabinet = models.ForeignKey(to=Cabinet, on_delete=models.CASCADE)
    position = models.ForeignKey(to=Position, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.first_name} {self.last_name} | {self.email} | {self.username}'

    class Meta:
        verbose_name = 'Сотрудник'
        verbose_name_plural = 'Сотрудники'
