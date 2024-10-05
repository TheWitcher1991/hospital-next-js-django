from django.db import models
from django.utils.translation import gettext_lazy as _

from business.defines import InvoiceTarget, PayerType, PaymentMethod, TransactionType
from core.models import BaseModel
from core.utils import decimal_to_words


class Invoice(BaseModel):
    payment_id = models.CharField(_("ID платежа YooKassa"), max_length=255, null=True, blank=True)
    payment_url = models.URLField(_("Ссылка на оплату"), blank=True, null=True)
    payment_method = models.CharField(
        _("Способ оплаты"),
        choices=PaymentMethod.choices,
        max_length=32,
        blank=True,
        null=True,
    )
    payer_type = models.CharField(
        _("Тип плательщика"), choices=PayerType.choices, max_length=32, default=PayerType.INDIVIDUAL
    )
    target = models.CharField(
        _("Цель оплаты"),
        choices=InvoiceTarget.choices,
        max_length=32,
    )
    description = models.CharField(_("Назначение платежа"), max_length=255, null=True, blank=True)
    amount = models.DecimalField(
        verbose_name=_("Сумма оплаты"),
        default=0,
        max_digits=10,
        decimal_places=2,
        null=True,
        blank=True,
    )
    is_paid = models.BooleanField(_("Оплачен"), default=False)
    expires_at = models.DateTimeField(
        _("Дата истечения срока действия"),
        blank=True,
        null=True,
    )
    captured_at = models.DateTimeField(
        _("Дата оплаты счета"),
        blank=True,
        null=True,
    )
    patient = models.ForeignKey(to="patient.Patient", related_name="invoices", on_delete=models.CASCADE)

    class Meta:
        verbose_name = _("Счет")
        verbose_name_plural = _("Счета")
        ordering = ("-created",)

    def __str__(self):
        return f"{self.patient.user.email} invoice: {self.amount}"

    @property
    def amount_in_words(self):
        return decimal_to_words(self.amount)


class InvoiceOrder(BaseModel):
    invoice = models.ForeignKey(to=Invoice, on_delete=models.CASCADE, related_name="services")
    service = models.ForeignKey(
        to="employee.Service",
        on_delete=models.CASCADE,
        related_name="orders",
    )
    quantity = models.PositiveIntegerField(_("Количество"), default=1)

    class Meta:
        verbose_name = "Услуга по счету"
        verbose_name_plural = "Услуги по счетам"

    def __str__(self):
        return f"{self.invoice} - {self.service} x {self.quantity}"

    def get_service_price(self):
        return self.service.price * self.quantity


class Transaction(BaseModel):
    amount = models.DecimalField(
        _("Сумма транзакции"),
        default=0,
        max_digits=10,
        decimal_places=2,
        null=True,
        blank=True,
    )
    transaction_type = models.CharField(
        _("Тип транзакции"),
        choices=TransactionType.choices,
        max_length=32,
    )
    description = models.CharField(_("Описание транзакции"), max_length=255, null=True, blank=True)
    invoice = models.ForeignKey(
        to=Invoice,
        related_name="transactions",
        on_delete=models.CASCADE,
        blank=True,
        null=True,
    )
    patient = models.ForeignKey(to="patient.Patient", related_name="transactions", on_delete=models.CASCADE)

    class Meta:
        verbose_name = _("Транзакция")
        verbose_name_plural = _("Транзакции")
        ordering = ("-created",)

    def __str__(self):
        return f"{self.patient.user.email} transaction: {self.amount}"

    @property
    def amount_in_words(self):
        return decimal_to_words(self.amount)
