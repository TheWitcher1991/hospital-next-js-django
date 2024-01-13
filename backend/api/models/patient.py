from django.contrib.auth.models import AbstractUser
from django.db import models


class PatientType(models.Model):
    name = models.CharField('Название', max_length=256)
    sale = models.IntegerField('Скидка', max_length=10)

    def __str__(self):
        return f'{self.name}, скидка - {self.sale}%'

    class Meta:
        verbose_name = 'Тип пациента'
        verbose_name_plural = 'Типы пациентов'


class Patient(AbstractUser):
    patronymic = models.CharField('Отчество', max_length=256)
    date = models.DateField('Дата рождения')
    address = models.CharField('Адрес', max_length=256)
    oms = models.CharField('ОМС', max_length=16)
    snils = models.CharField('СНИЛС', max_length=16)
    inn = models.CharField('ИНН', max_length=12)
    passport = models.CharField('Паспорт', max_length=128)
    age = models.CharField('Возраст', max_length=10, blank=True)
    patient_type = models.ForeignKey(to=PatientType, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.first_name} {self.last_name} | {self.email} | {self.username}'

    class Meta:
        verbose_name = 'Пациент'
        verbose_name_plural = 'Пациенты'


class PatientPhone(models.Model):
    phone = models.CharField('Телефон', max_length=20)
    patient = models.ForeignKey(to=Patient, on_delete=models.CASCADE)

    class Meta:
        verbose_name = 'Телефон'
        verbose_name_plural = 'Телефоны'


class PatientSignature(models.Model):
    signature = models.CharField('Открытый ключ', max_length=128)
    patient = models.ForeignKey(to=Patient, on_delete=models.CASCADE)

    class Meta:
        verbose_name = 'ЭЦП'
        verbose_name_plural = 'ЭЦП'
