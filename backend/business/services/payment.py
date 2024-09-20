import logging
from decimal import Decimal

from django.utils.timezone import now
from yookassa import Configuration, Payment
from yookassa.domain.response import PaymentListResponse, PaymentResponse

from config import settings

Configuration.account_id = settings.YOOKASSA_ACCOUNT_ID
Configuration.secret_key = settings.YOOKASSA_SECRET_KEY

logger = logging.getLogger("business")


class PaymentService:
    """
    Сервис для работы с платежами yookassa
    """

    def __init__(self):
        pass

    @property
    def is_test(self) -> bool:
        return settings.YOOKASSA_DEBUG

    @staticmethod
    def get_return_url() -> str:
        return f"{settings.YOOKASSA_RETURN_URL}"

    @staticmethod
    def create(payment_data: dict):
        try:
            return Payment.create(payment_data)
        except Exception as e:
            logger.error(f"ERROR: Ошибка при создании платежа {payment_data} {e} | {now()}")
            raise e

    @staticmethod
    def find_one(payment_id: str) -> PaymentResponse:
        try:
            return Payment.find_one(payment_id)
        except Exception as e:
            logger.error(f"ERROR: Ошибка при получении объекта payment {payment_id} {e} | {now()}")
            raise e

    @staticmethod
    def list() -> PaymentListResponse:
        try:
            return Payment.list()
        except Exception as e:
            logger.error(f"ERROR: Ошибка при получении списка платежей {e} | {now()}")
            raise e

    @staticmethod
    def capture(payment_id: str, payment_amount: Decimal, payment_currency: str = "RUB"):
        try:
            return Payment.capture(
                payment_id,
                {
                    "amount": {
                        "value": payment_amount,
                        "currency": payment_currency,
                    },
                },
            )
        except Exception as e:
            logger.error(f"ERROR: Ошибка при подтверждении платежа {payment_id} {e} | {now()}")
            raise e

    @staticmethod
    def cancel(payment_id: str):
        try:
            return Payment.cancel(payment_id)
        except Exception as e:
            logger.error(f"ERROR: Ошибка при отмене платежа {payment_id} {e} | {now()}")
            raise e
