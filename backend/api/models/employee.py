from django.db import models
from user import User
from position import Cabinet, Position


class Employee(models.Model):
    user = models.OneToOneField(to=User, on_delete=models.CASCADE, primary_key=True)
    cabinet = models.ForeignKey(to=Cabinet, on_delete=models.CASCADE)
    position = models.ForeignKey(to=Position, on_delete=models.CASCADE)

    objects = models.Manager()

    class Meta:
        verbose_name = 'Сотрудник'
        verbose_name_plural = 'Сотрудники'

    def __str__(self):
        return f'{self.user} | {self.position}'


