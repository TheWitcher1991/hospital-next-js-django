from decimal import Decimal

from django.core.validators import MinValueValidator
from django.db import models, transaction
from django.utils.translation import gettext_lazy as _
from rest_framework.generics import get_object_or_404

from core.decorators import is_amount_positive
from core.models import BaseModel

from .defines import PatientCartStatus
from .managers import (
    PatientCartActiveManager,
    PatientCartArchiveManager,
    PatientCartDraftManager,
    PatientCartWithOutDiagnoseManager,
)


class Patient(BaseModel):
    address = models.CharField(_("Адрес"), max_length=256, blank=True, null=True)
    oms = models.CharField(_("ОМС"), max_length=16)
    snils = models.CharField(_("СНИЛС"), max_length=16, blank=True, null=True)
    inn = models.CharField(_("ИНН"), max_length=12, blank=True, null=True)
    passport = models.CharField(_("Паспорт"), max_length=128, blank=True, null=True)
    user = models.OneToOneField(to="core.User", on_delete=models.CASCADE, related_name="patient")
    patient_type = models.ForeignKey(to="core.PatientType", on_delete=models.CASCADE, related_name="patients")

    class Meta:
        unique_together = ("oms", "snils", "inn", "passport", "user")
        verbose_name = _("Пациент")
        verbose_name_plural = _("Пациенты")

    def __str__(self):
        return f"{self.user} | {self.oms}"


class PatientBalance(BaseModel):
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


class PatientPhone(BaseModel):
    phone = models.CharField(_("Телефон"), max_length=20)
    patient = models.ForeignKey(to=Patient, on_delete=models.CASCADE, related_name="phones")

    class Meta:
        verbose_name = _("Телефон")
        verbose_name_plural = _("Телефоны")


class PatientSignature(BaseModel):
    signature = models.CharField(_("Открытый ключ"), max_length=128)
    patient = models.ForeignKey(to=Patient, on_delete=models.CASCADE, related_name="signatures")

    class Meta:
        unique_together = ("signature", "patient")
        verbose_name = _("ЭЦП")
        verbose_name_plural = _("ЭЦП")


class PatientCart(BaseModel):
    diagnose = models.CharField(_("Диагноз"), max_length=256, blank=True, null=True)
    date_visit = models.DateField(_("Дата визита"))
    status = models.CharField(
        _("Статус"), default=PatientCartStatus.DRAFT, choices=PatientCartStatus.choices, max_length=32
    )
    patient = models.ForeignKey(to=Patient, on_delete=models.CASCADE, related_name="carts")
    service = models.ForeignKey(to="employee.Service", on_delete=models.CASCADE, related_name="patient_carts")

    objects = models.Manager()
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


class Agreement(BaseModel):
    start = models.TimeField(_("Начало"))
    end = models.TimeField(_("Конец"))
    patient_cart = models.ForeignKey(to=PatientCart, on_delete=models.CASCADE, related_name="agreements")

    class Meta:
        verbose_name = _("Договор")
        verbose_name_plural = _("Договоры")


class Talon(BaseModel):
    result = models.TextField(_("Результат"))
    agreement = models.ForeignKey(to=Agreement, on_delete=models.CASCADE, related_name="talons")

    class Meta:
        verbose_name = _("Талон")
        verbose_name_plural = _("Талоны")
