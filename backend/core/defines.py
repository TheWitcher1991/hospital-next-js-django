from django.db import models
from django.utils.translation import gettext_lazy as _


class Role(models.TextChoices):
    PATIENT = "PATIENT", _("Пациент")
    EMPLOYEE = "EMPLOYEE", _("Сотрудник")
    GUEST = "GUEST", _("Гость")


class Floor(models.TextChoices):
    MALE = "MALE", _("Мужской")
    FEMALE = "FEMALE", _("Женский")


class CeleryQueue:
    DEFAULT = "celery"
    PATIENT = "patient"
    EMPLOYEE = "employee"
    BUSINESS = "business"
