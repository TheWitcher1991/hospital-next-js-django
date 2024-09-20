import logging
from typing import Type

from django.db import transaction
from django.db.models import QuerySet
from django.utils import timezone
from rest_framework.generics import get_object_or_404
from yookassa.domain.response import PaymentResponse

from business.defines import PaymentMethod
from business.models import Invoice
from business.services.payment import PaymentService
from config import settings
from core.exceptions import ModelNotDeletedException

logger = logging.getLogger("business")


class InvoiceService:
    """
    Сервис для работы со счетами на оплату
    """

    def __int__(self):
        pass

    def get_by_id(self, invoice_id: int) -> Invoice:
        try:
            return get_object_or_404(Invoice, id=invoice_id)
        except Exception as e:
            logger.error(f"ERROR: Ошибка при получении объекта invoice {invoice_id} {e}")
            raise e

    def get_expired(self) -> QuerySet:
        return Invoice.objects.filter(is_paid=False, expires_at__lt=timezone.now())

    def factory_receipt(self, invoice: Invoice) -> dict | None:
        receipt = None

        receipt = {
            "customer": {"email": invoice.patient.user.email},
            "items": [],
            "settlements": [],
        }

        return receipt

    def get_description(self, invoice: Invoice) -> str:
        return f"Оплата за интернет-услуги по счёту № {invoice.id} от {invoice.created.strftime('%d.%m.%Y')}, без НДС"

    def create(self, data: dict) -> Invoice:
        pass

    def capture(self, invoice_id: int) -> Type[NotImplementedError] | bool:
        pass

    def cancel(self, invoice_id: int) -> bool:
        try:
            with transaction.atomic():
                invoice = InvoiceService.get_by_id(invoice_id=invoice_id)

                if invoice.payment_id:
                    PaymentService.cancel(invoice.payment_id)

                invoice.delete()

                return True
        except (Exception, ModelNotDeletedException) as e:
            logger.error(f"ERROR: Ошибка при отмене счёта {invoice_id} {e}")
            raise e

    def get_payment_type(self, method):
        return None if method in [PaymentMethod.CASHLESS, PaymentMethod.BALANCE] else method

    def create_payment(self, invoice: Invoice) -> PaymentResponse:
        try:
            return_url = PaymentService.get_return_url()
            payment_type = self.get_payment_type(invoice.payment_method)
            receipt = self.factory_receipt(invoice)

            payment = PaymentService.create(
                {
                    "amount": {
                        "value": invoice.amount,
                        "currency": "RUB",
                    },
                    "payment_method_data": {
                        "type": payment_type,
                    },
                    "confirmation": {
                        "type": "redirect",
                        "return_url": f"{return_url}?invoice={invoice.id}",
                    },
                    "metadata": {
                        "invoice_id": invoice.id,
                        "patient_id": invoice.patient.id,
                    },
                    "receipt": {
                        **receipt,
                    },
                    "capture": True,
                    "description": self.get_description(invoice),
                }
            )

            invoice.payment_id = payment.id
            invoice.payment_method = payment.payment_method.type
            invoice.payment_url = payment.confirmation.confirmation_url

            if payment.expires_at:
                invoice.expires_at = payment.expires_at
            else:
                invoice.expires_at = timezone.now() + timezone.timedelta(days=settings.PAYMENT_DAYS_TO_EXPIRE)

            invoice.save()

            return payment
        except Exception as e:
            logger.error(f"ERROR: Ошибка при создании платежа yookassa для счета {invoice.id} {e}")
            raise e
