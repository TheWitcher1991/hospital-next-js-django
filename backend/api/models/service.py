from django.db import models
from employee import Employee


class ServiceType(models.Model):
    name = models.CharField('Название', max_length=128, unique=True)

    class Meta:
        verbose_name = 'Специализация'
        verbose_name_plural = 'Специализации'


class ServiceFreeManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset().filter(price=0)


class Service(models.Model):
    name = models.CharField('Название', max_length=128, unique=True)
    price = models.DecimalField('Цена', max_digits=10, decimal_places=0, default=0)
    employee = models.ForeignKey(to=Employee, on_delete=models.CASCADE)
    service_type = models.ForeignKey(to=ServiceType, on_delete=models.CASCADE)

    objects = models.Manager()
    free = ServiceFreeManager()

    def __str__(self):
        return f'{self.name} | {self.price} руб.'

    class Meta:
        verbose_name = 'Услуга'
        verbose_name_plural = 'Услуги'

