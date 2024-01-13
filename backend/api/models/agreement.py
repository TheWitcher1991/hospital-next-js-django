from django.db import models
from patientcart import PatientCart


class Agreement(models.Model):
    start = models.TimeField('Начало')
    end = models.TimeField('Конец')
    patient_cart = models.ForeignKey(to=PatientCart, on_delete=models.CASCADE)

    class Meta:
        verbose_name = 'Договор'
        verbose_name_plural = 'Договоры'


class Talon(models.Model):
    result = models.TextField('Результат')
    agreement = models.ForeignKey(to=Agreement, on_delete=models.CASCADE)

    class Meta:
        verbose_name = 'Талон'
        verbose_name_plural = 'Талоны'
