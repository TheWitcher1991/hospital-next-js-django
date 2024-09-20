from decimal import Decimal

from yookassa import Configuration, Payment
from yookassa.domain.response import PaymentResponse

from config.celery import BaseTaskWithRetry, app
from config.settings import YOOKASSA_ACCOUNT_ID, YOOKASSA_RETURN_URL, YOOKASSA_SECRET_KEY
from core.utils import queryset_ids

from .defines import PaymentMethod
from .services.invoices import InvoiceService

invoice_service = InvoiceService()

Configuration.account_id = YOOKASSA_ACCOUNT_ID
Configuration.secret_key = YOOKASSA_SECRET_KEY


@app.task(bind=True, base=BaseTaskWithRetry)
def check_expired_invoices_task(self):
    invoices = invoice_service.get_expired()
    # job = group(cancel_expired_invoices_task.s(invoice) for invoice in invoices)
    cancel_expired_invoices_task.chunks([(invoice,) for invoice in queryset_ids(invoices)], 10).apply_async()


@app.task(bind=True, base=BaseTaskWithRetry)
def cancel_expired_invoices_task(self, invoice_id):
    try:
        invoice_service.cancel(invoice_id)
    except Exception as e:
        raise Exception(e)


@app.task(bind=True, trail=True, autoretry_for=(Exception,), retry_kwargs={"max_retries": 3, "countdown": 10})
def payment_create_task(
    self,
    amount: Decimal,
    payment_method: PaymentMethod,
    description: str,
    return_url: str = YOOKASSA_RETURN_URL,
    receipt: dict | None = None,
    metadata: dict | None = None,
) -> PaymentResponse:
    try:
        payment = Payment.create(
            {
                "amount": {
                    "value": amount,
                    "currency": "RUB",
                },
                "payment_method_data": {"type": payment_method},
                "confirmation": {
                    "type": "redirect",
                    "return_url": return_url,
                },
                "receipt": receipt,
                "metadata": metadata,
                "capture": True,
                "description": description,
            }
        )
        return payment
    except Exception as e:
        raise Exception(e)


@app.task(bind=True, autoretry_for=(Exception,), retry_kwargs={"max_retries": 3, "countdown": 10})
def payment_capture_task(self, payment_id: str, payment_amount: str) -> None:
    try:
        Payment.capture(
            payment_id,
            {
                "amount": {
                    "value": payment_amount,
                    "currency": "RUB",
                },
            },
        )
    except Exception as e:
        raise Exception(e)


@app.task(bind=True, trail=True, autoretry_for=(Exception,), retry_kwargs={"max_retries": 3, "countdown": 10})
def payment_cancel_task(self, payment_id: str) -> None:
    try:
        Payment.cancel(payment_id)
    except Exception as e:
        raise Exception(e)


@app.task(bind=True, autoretry_for=(Exception,), retry_kwargs={"max_retries": 3, "countdown": 10})
def payment_find_one_task(self, payment_id: str) -> PaymentResponse:
    try:
        response = Payment.find_one(payment_id)
        return response
    except Exception as e:
        raise Exception(e)
