from django.contrib.auth.models import AbstractUser, PermissionsMixin
from django.db import models


class UserPatient(models.Manager):
    def get_queryset(self):
        return super().get_queryset().filter(type=0)


class UserEmployee(models.Manager):
    def get_queryset(self):
        return super().get_queryset().filter(type=1)


class User(AbstractUser, PermissionsMixin):
    class Type(models.IntegerChoices):
        PATIENT = 0, 'Пациент'
        EMPLOYEE = 1, 'Сотрудник'

    email = models.EmailField('Email', max_length=256, unique=True)
    first_name = models.CharField('Имя', max_length=256)
    last_name = models.CharField('Фамилия', max_length=256)
    patronymic = models.CharField('Отчество', max_length=256)
    age = models.CharField('Возраст', max_length=10, blank=True)
    date = models.DateField('Дата рождения')
    type = models.SmallIntegerField('Тип', choices=Type.choices)

    objects = models.Manager()
    patients = UserPatient()
    employees = UserEmployee()

    USERNAME_FIELD = email
    REQUIRED_FIELDS = ['first_name', 'last_name', 'patronymic']

    class Meta:
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'

    def get_full_name(self):
        return f'{self.last_name} {self.first_name} {self.patronymic}'

    def __str__(self):
        return f'{self.type} | {self.last_name} | {self.first_name}'
