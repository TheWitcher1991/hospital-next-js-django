from django.contrib.auth.models import PermissionsMixin, AbstractUser

from .managers import *


class User(AbstractUser, PermissionsMixin):
    class Type(models.TextChoices):
        PATIENT = 'П', 'Пациент'
        EMPLOYEE = 'С', 'Сотрудник'

    class Floor(models.TextChoices):
        MALE = 'М', 'Мужской'
        FAMALE = 'Ж', 'Женский'

    email = models.EmailField('Email', max_length=256, unique=True)
    first_name = models.CharField('Имя', max_length=256)
    last_name = models.CharField('Фамилия', max_length=256)
    patronymic = models.CharField('Отчество', max_length=256)
    age = models.CharField('Возраст', max_length=10, blank=True, null=True)
    date = models.DateField('Дата рождения')
    type = models.CharField('Тип', choices=Type.choices, max_length=1)
    gender = models.CharField('Пол', choices=Floor.choices, max_length=1)

    objects = models.Manager()
    patients = UserPatient()
    employees = UserEmployee()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['first_name', 'last_name', 'patronymic']

    class Meta:
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'

    def get_full_name(self):
        return f'{self.last_name} {self.first_name} {self.patronymic}'

    def __str__(self):
        return f'{self.get_type_display()} | {self.last_name} | {self.first_name}'
    

class PatientType(models.Model):
    name = models.CharField('Название', max_length=256)
    sale = models.CharField('Скидка', max_length=10)

    objects = models.Manager()

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

    objects = models.Manager()

    class Meta:
        verbose_name = 'Телефон'
        verbose_name_plural = 'Телефоны'


class PatientSignature(models.Model):
    signature = models.CharField('Открытый ключ', max_length=128, unique=True)
    patient = models.ForeignKey(to=Patient, on_delete=models.CASCADE)

    objects = models.Manager()

    class Meta:
        verbose_name = 'ЭЦП'
        verbose_name_plural = 'ЭЦП'
    
    
class Position(models.Model):
    name = models.CharField('Название', max_length=256)
    functions = models.TextField('Функции')
    salary = models.DecimalField('Зарплата', max_digits=10, decimal_places=0)

    objects = models.Manager()

    class Meta:
        verbose_name = 'Должность'
        verbose_name_plural = 'Должности'
        
    def __str__(self):
        return f'{self.name} | {self.salary} руб.'


class Cabinet(models.Model):
    name = models.CharField('Название', max_length=256)
    number = models.CharField('Номер', max_length=10)

    objects = models.Manager()

    class Meta:
        verbose_name = 'Кабинет'
        verbose_name_plural = 'Кабинеты'
    
    def __str__(self):
        return f'{self.name} | {self.number}'


class Shift(models.Model):
    number = models.CharField('Номер смены', max_length=10)
    start = models.TimeField('Старт смены')
    end = models.TimeField('Конец смены')

    objects = models.Manager()

    class Meta:
        verbose_name = 'Смена'
        verbose_name_plural = 'Смены'

    def __str__(self):
        return f'{self.number} | {self.start} - {self.end}'


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


class Schedule(models.Model):
    date = models.DateField('Дата графика работы')
    shift = models.ForeignKey(to=Shift, on_delete=models.CASCADE)
    employee = models.ForeignKey(to=Employee, on_delete=models.CASCADE)

    objects = models.Manager()

    class Meta:
        verbose_name = 'График работы'
        verbose_name_plural = 'График работы'


class ServiceType(models.Model):
    name = models.CharField('Название', max_length=128, unique=True)

    objects = models.Manager()

    class Meta:
        verbose_name = 'Специализация'
        verbose_name_plural = 'Специализации'


class Service(models.Model):
    name = models.CharField('Название', max_length=128, unique=True)
    price = models.DecimalField('Цена', max_digits=10, decimal_places=0, default=0)
    employee = models.ForeignKey(to=Employee, on_delete=models.CASCADE)
    service_type = models.ForeignKey(to=ServiceType, on_delete=models.CASCADE)

    objects = models.Manager()
    free = ServiceFreeManager()

    class Meta:
        verbose_name = 'Услуга'
        verbose_name_plural = 'Услуги'
        
    def __str__(self):
        return f'{self.name} | {self.price} руб.'


class PatientCart(models.Model):
    class Status(models.TextChoices):
        DRAFT = '0', 'Черновик'
        ACTIVE = '1', 'Обслуживание'
        ARCHIVE = '2', 'Архив'

    diagnose = models.CharField('Диагноз', max_length=256, blank=True, null=True)
    date_visit = models.DateField('Дата визита')
    created = models.DateTimeField('Дата', auto_now_add=True)
    status = models.CharField('Статус', default='0', choices=Status.choices, max_length=1)
    patient = models.ForeignKey(to=Patient, on_delete=models.CASCADE)
    service = models.ForeignKey(to=Service, on_delete=models.CASCADE)

    objects = models.Manager()
    drafts = PatientCartDraftManager()
    actives = PatientCartActiveManager()
    archive = PatientCartArchiveManager()
    withOutDiagnose = PatientCartWithOutDiagnoseManager()

    class Meta:
        verbose_name = 'Амбулаторная карта'
        verbose_name_plural = 'Амбулаторные карты'
        ordering = ['-created']
        indexes = [
            models.Index(fields=['-created'])
        ]

    def __str__(self):
        return f'{self.get_status_display()} | {self.date_visit}'
    
    
class Agreement(models.Model):
    start = models.TimeField('Начало')
    end = models.TimeField('Конец')
    patient_cart = models.ForeignKey(to=PatientCart, on_delete=models.CASCADE)

    objects = models.Manager()

    class Meta:
        verbose_name = 'Договор'
        verbose_name_plural = 'Договоры'


class Talon(models.Model):
    result = models.TextField('Результат')
    agreement = models.ForeignKey(to=Agreement, on_delete=models.CASCADE)

    objects = models.Manager()

    class Meta:
        verbose_name = 'Талон'
        verbose_name_plural = 'Талоны'
        