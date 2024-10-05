from django.contrib.auth.models import AbstractUser, PermissionsMixin
from django.core.mail import send_mail
from django.db import models
from django.utils.timezone import now
from django.utils.translation import gettext_lazy as _

from .defines import Floor, Role
from .managers import UserEmployee, UserManager, UserPatient


class User(AbstractUser, PermissionsMixin):
    email = models.EmailField(_("Email"), max_length=256, unique=True)
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

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ["phone"]

    objects = UserManager()
    patients = UserPatient()
    employees = UserEmployee()

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


class BaseModel(models.Model):
    created = models.DateTimeField(_("Дата создания"), auto_now_add=True)
    updated = models.DateTimeField(_("Дата обновления"), auto_now=True)

    class Meta:
        abstract = True


class Session(BaseModel):
    access_token = models.CharField(max_length=1024)
    refresh_token = models.CharField(max_length=1024)
    refresh_token_expires = models.DateTimeField(null=True, blank=True)
    ip = models.CharField(_("IP-адрес"), max_length=255)
    user_agent = models.CharField("User-Agent", max_length=255)
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


class PatientType(BaseModel):
    name = models.CharField(_("Название"), max_length=256)
    sale = models.CharField(_("Скидка"), max_length=10)

    class Meta:
        verbose_name = _("Тип пациента")
        verbose_name_plural = _("Типы пациентов")

    def __str__(self):
        return f"{self.name} | скидка - {self.sale}%"


class Position(BaseModel):
    name = models.CharField(_("Название"), max_length=256)
    functions = models.TextField(_("Функции"))
    salary = models.DecimalField("Зарплата", max_digits=10, decimal_places=0)

    class Meta:
        verbose_name = _("Должность")
        verbose_name_plural = _("Должности")

    def __str__(self):
        return f"{self.name} | {self.salary} руб."


class Cabinet(BaseModel):
    name = models.CharField(_("Название"), max_length=256)
    number = models.CharField(_("Номер"), max_length=10)

    class Meta:
        verbose_name = _("Кабинет")
        verbose_name_plural = _("Кабинеты")

    def __str__(self):
        return f"{self.name} | {self.number}"


class ServiceType(BaseModel):
    name = models.CharField(_("Название"), max_length=128)
    ico = models.CharField(_("Иконка mdi-icons"), max_length=128, blank=True, null=True)

    class Meta:
        unique_together = ("name", "ico")
        verbose_name = _("Специализация")
        verbose_name_plural = _("Специализации")

    def __str__(self):
        return self.name
