from django.db import models
from user import User


class PatientType(models.Model):
    name = models.CharField('Название', max_length=256)
    sale = models.IntegerField('Скидка', max_length=10)

    class Meta:
        verbose_name = 'Тип пациента'
        verbose_name_plural = 'Типы пациентов'

    def __str__(self):
        return f'{self.name} | скидка - {self.sale}%'


class Patient(models.Model):
    address = models.CharField('Адрес', max_length=256)
    oms = models.CharField('ОМС', max_length=16, unique=True)
    snils = models.CharField('СНИЛС', max_length=16, unique=True)
    inn = models.CharField('ИНН', max_length=12, unique=True)
    passport = models.CharField('Паспорт', max_length=128, unique=True)
    user = models.OneToOneField(to=User, on_delete=models.CASCADE, primary_key=True)
    patient_type = models.ForeignKey(to=PatientType, on_delete=models.CASCADE)

    objects = models.Manager()

    class Meta:
        verbose_name = 'Пациент'
        verbose_name_plural = 'Пациенты'

    def __str__(self):
        return f'{self.user} | {self.oms}'


class PatientPhone(models.Model):
    phone = models.CharField('Телефон', max_length=20)
    patient = models.ForeignKey(to=Patient, on_delete=models.CASCADE)

    class Meta:
        verbose_name = 'Телефон'
        verbose_name_plural = 'Телефоны'


class PatientSignature(models.Model):
    signature = models.CharField('Открытый ключ', max_length=128, unique=True)
    patient = models.ForeignKey(to=Patient, on_delete=models.CASCADE)

    class Meta:
        verbose_name = 'ЭЦП'
        verbose_name_plural = 'ЭЦП'
