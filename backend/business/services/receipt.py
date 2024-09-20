import logging

from django.utils.timezone import now
from yookassa import Configuration, Receipt
from yookassa.domain.response import ReceiptListResponse, ReceiptResponse

from config import settings

Configuration.account_id = settings.YOOKASSA_ACCOUNT_ID
Configuration.secret_key = settings.YOOKASSA_SECRET_KEY

logger = logging.getLogger("business")


class ReceiptService:
    """
    Сервис для работы с чеками yookassa
    """

    def __init__(self):
        pass

    @staticmethod
    def create(receipt_data: dict) -> ReceiptResponse:
        try:
            return Receipt.create(receipt_data)
        except Exception as e:
            logger.error(f"ERROR: Ошибка при создании чека {receipt_data} {e} | {now()}")
            raise e

    @staticmethod
    def get(receipt_id) -> ReceiptResponse:
        try:
            return Receipt.find_one(receipt_id)
        except Exception as e:
            logger.error(f"ERROR: Ошибка при получении чека {receipt_id} {e} | {now()}")
            raise e

    @staticmethod
    def list(params=None) -> ReceiptListResponse:
        if params is None:
            params = {}
        try:
            return Receipt.list(params)
        except Exception as e:
            logger.error(f"ERROR: Ошибка при получении списка чеков {e} | {now()}")
            raise e
