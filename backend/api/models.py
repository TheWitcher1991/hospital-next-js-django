from decimal import Decimal

from django.contrib.auth.models import AbstractUser, PermissionsMixin
from django.core.mail import send_mail
from django.core.validators import MinValueValidator
from django.db import models, transaction
from django.utils.timezone import now
from django.utils.translation import gettext_lazy as _
from rest_framework.generics import get_object_or_404

from .decorators import is_amount_positive
from .defines import Floor, PatientCartStatus, Role
from .managers import (
    PatientCartActiveManager,
    PatientCartArchiveManager,
    PatientCartDraftManager,
    PatientCartWithOutDiagnoseManager,
    ServiceFreeManager,
    UserEmployee,
    UserPatient,
)


class User(AbstractUser, PermissionsMixin):
    email = models.EmailField(_("Email"), max_length=256)
    phone = models.CharField(_("Телефон"), max_length=20, blank=True, null=True)
    password = models.CharField(_("Пароль"), max_length=256)
    first_name = models.CharField(_("Имя"), max_length=256)
    last_name = models.CharField(_("Фамилия"), max_length=256)
    patronymic = models.CharField(_("Отчество"), max_length=256)
    age = models.CharField(_("Возраст"), max_length=10, blank=True, null=True)
    date = models.DateField(_("Дата рождения"))
    date_joined = models.DateTimeField(_("Создан"), auto_now_add=True)
    updated_at = models.DateTimeField(_("Обновлен"), auto_now=True)
    is_active = models.BooleanField(_("Активность"), default=True)
    is_staff = models.BooleanField(_("Администратор"), default=False)
    is_online = models.BooleanField(_("Онлайн"), default=False)
    role = models.CharField(_("Роль"), choices=Role.choices, max_length=32, default=Role.PATIENT)
    gender = models.CharField(_("Пол"), choices=Floor.choices, max_length=12)
    last_ip = models.CharField(_("Последний IP-адрес"), max_length=255, blank=True, null=True)
    last_online = models.DateTimeField(_("Последняя активность"), blank=True, null=True)

    patients = UserPatient()
    employees = UserEmployee()

    EMAIL_FIELD = "email"
    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []

    class Meta:
        unique_together = ("email", "phone")
        verbose_name = _("Пользователь")
        verbose_name_plural = _("Пользователи")
        indexes = [
            models.Index(fields=["email", "phone"]),
            models.Index(fields=["first_name", "last_name", "patronymic"]),
            models.Index(fields=["date_joined", "updated_at"]),
        ]

    # def profile(self):
    #    return Patient.objects.get(user=self) if self.role == 'П' else Employee.objects.get(user=self)

    def clean(self):
        super().clean()
        self.email = self.__class__.objects.normalize_email(self.email)

    def get_full_name(self):
        return f"{self.last_name} {self.first_name} {self.patronymic}"

    def get_short_name(self):
        return self.first_name

    def email_user(self, subject, message, from_email=None, **kwargs):
        send_mail(subject, message, from_email, [self.email], **kwargs)

    def __str__(self):
        return f"{self.get_role_display()} | {self.last_name} | {self.first_name}"


class Session(models.Model):
    access_token = models.CharField(max_length=1024)
    refresh_token = models.CharField(max_length=1024)
    refresh_token_expires = models.DateTimeField(null=True, blank=True)
    ip = models.CharField(_("IP-адрес"), max_length=255)
    user_agent = models.CharField("User-Agent", max_length=255)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="sessions")

    class Meta:
        unique_together = ("access_token", "refresh_token")
        verbose_name = _("Сессия")
        verbose_name_plural = _("Сессии")
        ordering = ["-created"]
        indexes = [models.Index(fields=["created"])]

    def __str__(self):
        return f"{self.user} - {self.ip}"

    @property
    def expired(self):
        return self.refresh_token_expires < now()


class PatientType(models.Model):
    name = models.CharField(_("Название"), max_length=256)
    sale = models.CharField(_("Скидка"), max_length=10)

    class Meta:
        verbose_name = _("Тип пациента")
        verbose_name_plural = _("Типы пациентов")

    def __str__(self):
        return f"{self.name} | скидка - {self.sale}%"


class Patient(models.Model):
    address = models.CharField(_("Адрес"), max_length=256)
    oms = models.CharField(_("ОМС"), max_length=16)
    snils = models.CharField(_("СНИЛС"), max_length=16)
    inn = models.CharField(_("ИНН"), max_length=12)
    passport = models.CharField(_("Паспорт"), max_length=128)
    user = models.OneToOneField(to=User, on_delete=models.CASCADE, related_name="patient")
    patient_type = models.ForeignKey(to=PatientType, on_delete=models.CASCADE)

    class Meta:
        unique_together = ("oms", "snils", "inn", "passport", "user")
        verbose_name = _("Пациент")
        verbose_name_plural = _("Пациенты")

    def __str__(self):
        return f"{self.user} | {self.oms}"


class PatientBalance(models.Model):
    balance = models.DecimalField(
        _("Остаток средств"),
        max_digits=10,
        decimal_places=2,
        validators=[MinValueValidator(0, message="Balance cannot be negative")],
    )
    patient = models.OneToOneField(to=Patient, on_delete=models.CASCADE, related_name="balance")

    class Meta:
        verbose_name = _("Баланс пациента")
        verbose_name_plural = _("Балансы пациентов")

    def __str__(self):
        return f"{self.patient.user} balance: {self.balance}"

    @classmethod
    @is_amount_positive
    def deposit(cls, *, pk: int, amount: Decimal):
        with transaction.atomic():
            balance = get_object_or_404(cls.objects.select_for_update(), pk=pk)
            balance.balance += amount
            balance.save()
        return balance

    @classmethod
    @is_amount_positive
    def withdraw(cls, *, pk: int, amount: Decimal):
        with transaction.atomic():
            balance = get_object_or_404(cls.objects.select_for_update(), pk=pk)
            balance.balance -= amount
            balance.save()
        return balance


class PatientPhone(models.Model):
    phone = models.CharField(_("Телефон"), max_length=20)
    patient = models.ForeignKey(to=Patient, on_delete=models.CASCADE)

    class Meta:
        verbose_name = _("Телефон")
        verbose_name_plural = _("Телефоны")


class PatientSignature(models.Model):
    signature = models.CharField(_("Открытый ключ"), max_length=128)
    patient = models.ForeignKey(to=Patient, on_delete=models.CASCADE)

    class Meta:
        unique_together = ("signature", "patient")
        verbose_name = _("ЭЦП")
        verbose_name_plural = _("ЭЦП")


class Position(models.Model):
    name = models.CharField(_("Название"), max_length=256)
    functions = models.TextField(_("Функции"))
    salary = models.DecimalField("Зарплата", max_digits=10, decimal_places=0)

    class Meta:
        verbose_name = _("Должность")
        verbose_name_plural = _("Должности")

    def __str__(self):
        return f"{self.name} | {self.salary} руб."


class Cabinet(models.Model):
    name = models.CharField(_("Название"), max_length=256)
    number = models.CharField(_("Номер"), max_length=10)

    class Meta:
        verbose_name = _("Кабинет")
        verbose_name_plural = _("Кабинеты")

    def __str__(self):
        return f"{self.name} | {self.number}"


class Shift(models.Model):
    number = models.CharField(_("Номер смены"), max_length=10)
    start = models.TimeField(_("Старт смены"))
    end = models.TimeField(_("Конец смены"))

    class Meta:
        verbose_name = _("Смена")
        verbose_name_plural = _("Смены")

    def __str__(self):
        return f"{self.number} | {self.start} - {self.end}"


class Employee(models.Model):
    user = models.OneToOneField(to=User, on_delete=models.CASCADE, related_name="employee")
    cabinet = models.ForeignKey(to=Cabinet, on_delete=models.CASCADE)
    position = models.ForeignKey(to=Position, on_delete=models.CASCADE)

    class Meta:
        verbose_name = _("Сотрудник")
        verbose_name_plural = _("Сотрудники")

    def __str__(self):
        return f"{self.user} | {self.position}"


class Schedule(models.Model):
    date = models.DateField(_("Дата графика работы"))
    shift = models.ForeignKey(to=Shift, on_delete=models.CASCADE)
    employee = models.ForeignKey(to=Employee, on_delete=models.CASCADE)

    class Meta:
        verbose_name = _("График работы")
        verbose_name_plural = _("График работы")

    def __str__(self):
        return f"{self.date} | {self.employee} | {self.shift}"


class ServiceType(models.Model):
    name = models.CharField(_("Название"), max_length=128)
    ico = models.CharField(_("Иконка mdi-icons"), max_length=128, blank=True, null=True)

    class Meta:
        unique_together = ("name", "ico")
        verbose_name = _("Специализация")
        verbose_name_plural = _("Специализации")

    def __str__(self):
        return self.name


class Service(models.Model):
    name = models.CharField(_("Название"), max_length=128)
    price = models.DecimalField(_("Цена"), max_digits=10, decimal_places=2, default=0)
    employee = models.ForeignKey(to=Employee, on_delete=models.CASCADE)
    service_type = models.ForeignKey(to=ServiceType, on_delete=models.CASCADE)

    free = ServiceFreeManager()

    class Meta:
        unique_together = ("name", "service_type")
        verbose_name = _("Услуга")
        verbose_name_plural = _("Услуги")

    def __str__(self):
        return f"{self.name} | {self.price} руб."


class PatientCart(models.Model):
    diagnose = models.CharField(_("Диагноз"), max_length=256, blank=True, null=True)
    date_visit = models.DateField(_("Дата визита"))
    created = models.DateTimeField(_("Дата"), auto_now_add=True)
    status = models.CharField(
        _("Статус"), default=PatientCartStatus.DRAFT, choices=PatientCartStatus.choices, max_length=32
    )
    patient = models.ForeignKey(to=Patient, on_delete=models.CASCADE)
    service = models.ForeignKey(to=Service, on_delete=models.CASCADE)

    drafts = PatientCartDraftManager()
    actives = PatientCartActiveManager()
    archive = PatientCartArchiveManager()
    withOutDiagnose = PatientCartWithOutDiagnoseManager()

    class Meta:
        verbose_name = _("Амбулаторная карта")
        verbose_name_plural = _("Амбулаторные карты")
        ordering = ["-created"]
        indexes = [models.Index(fields=["-created"])]

    def __str__(self):
        return f"{self.get_status_display()} | {self.date_visit}"


class Agreement(models.Model):
    start = models.TimeField(_("Начало"))
    end = models.TimeField(_("Конец"))
    patient_cart = models.ForeignKey(to=PatientCart, on_delete=models.CASCADE)

    class Meta:
        verbose_name = _("Договор")
        verbose_name_plural = _("Договоры")


class Talon(models.Model):
    result = models.TextField(_("Результат"))
    agreement = models.ForeignKey(to=Agreement, on_delete=models.CASCADE)

    class Meta:
        verbose_name = _("Талон")
        verbose_name_plural = _("Талоны")
