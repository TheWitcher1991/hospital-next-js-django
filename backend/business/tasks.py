from decimal import Decimal

from yookassa import Configuration, Payment
from yookassa.domain.response import PaymentResponse

from config.celery import app
from config.settings import YOOKASSA_ACCOUNT_ID, YOOKASSA_RETURN_URL, YOOKASSA_SECRET_KEY

from .defines import PaymentMethod

Configuration.account_id = YOOKASSA_ACCOUNT_ID
Configuration.secret_key = YOOKASSA_SECRET_KEY


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
