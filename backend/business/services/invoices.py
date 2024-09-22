import logging
from typing import Type

from django.db import transaction
from django.db.models import QuerySet
from django.utils import timezone
from rest_framework.generics import get_object_or_404
from yookassa.domain.response import PaymentResponse

from business.defines import InvoiceTarget, PaymentMethod
from business.exceptions import InsufficientBalanceException
from business.models import Invoice, InvoiceOrder
from business.services.payment import PaymentService
from business.services.transaction import TransactionService
from config import settings
from core.exceptions import ModelNotDeletedException
from employee.models import Service
from patient.models import PatientBalance

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

    def get_service_by_id(self, service_id: int) -> Service:
        try:
            return get_object_or_404(Service, id=service_id)
        except Exception as e:
            logger.error(f"ERROR: Ошибка при получении объекта service {service_id} {e}")
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

    def calculate_amount(self, invoice: Invoice):
        try:
            total_amount = sum(order.get_service_price() for order in invoice.services.all())
            invoice.amount = total_amount
            invoice.save()
        except Exception as e:
            logger.error(f"ERROR: Ошибка при расчёте суммы по счёту {invoice.id} {e}")

    def create(self, data: dict) -> Invoice:
        with transaction.atomic():
            services = data.pop("services", [])
            invoice = Invoice.objects.create(**data)

            description = self.get_description(invoice)

            for service in services:
                s = self.get_service_by_id(service["service_id"])
                quantity = service.get("quantity", 1)
                InvoiceOrder.objects.create(
                    invoice=invoice,
                    service=s,
                    quantity=quantity,
                )

            self.calculate_amount(invoice)

            self.create_payment(invoice)

            if invoice.target == InvoiceTarget.BALANCE:
                description = (
                    f"Зачисление на Лицевой счёт по Договору № {invoice.patient.id}"
                    f" от {invoice.patient.user.date_joined.strftime('%d.%m.%Y')}"
                )

            if invoice.target == InvoiceTarget.SERVICE:
                description = (
                    f"Оплата медицинских услуг по Договору № {invoice.patient.id} "
                    f"от {invoice.patient.user.date_joined.strftime('%d.%m.%Y')}"
                )

            invoice.description = description
            invoice.save()

            return invoice

    def capture(self, invoice_id: int) -> Type[NotImplementedError] | bool:
        with transaction.atomic():
            invoice = self.get_by_id(invoice_id)

            if invoice.is_paid:
                invoice.captured_at = timezone.now()
                invoice.save()
                return True

            if invoice.target == InvoiceTarget.BALANCE:
                return NotImplementedError
            if invoice.target == InvoiceTarget.SERVICE:
                if invoice.patient.balance.balance < invoice.amount:
                    raise InsufficientBalanceException(
                        f"Недостаточно средств на балансе. "
                        f"Не хватает {invoice.amount - invoice.patient.balance.balance}"
                    )

            invoice.is_paid = True
            invoice.captured_at = timezone.now()
            invoice.save()

            if invoice.payment_id:
                PaymentService.capture(invoice.payment_id, invoice.amount)

            PatientBalance.withdraw(
                pk=invoice.patient.balance.id,
                amount=invoice.amount,
            )

            TransactionService.withdraw(
                amount=invoice.amount,
                description=invoice.description,
                invoice=invoice,
                patient=invoice.patient,
                created=invoice.captured_at,
            )

            return True

    def cancel(self, invoice_id: int) -> bool:
        try:
            with transaction.atomic():
                invoice = self.get_by_id(invoice_id)

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
