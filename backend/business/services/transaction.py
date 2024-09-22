import logging

from django.db.models import Sum

from business.defines import TransactionType
from business.models import Transaction
from core.exceptions import ModelNotCreatedException

logger = logging.getLogger("business")


class TransactionService:
    """
    Сервис для работы с транзакциями
    """

    def __init__(self):
        pass

    @staticmethod
    def count_all(patient_id: int):
        return Transaction.objects.filter(patient_id=patient_id).count()

    @staticmethod
    def count_deposit(patient_id: int):
        return Transaction.objects.filter(patient_id=patient_id, transaction_type=TransactionType.DEPOSIT).aggregate(
            sum=Sum("amount")
        )["sum"]

    @staticmethod
    def count_withdrawal(patient_id: int):
        return Transaction.objects.filter(patient_id=patient_id, transaction_type=TransactionType.WITHDRAWAL).aggregate(
            sum=Sum("amount")
        )["sum"]

    @staticmethod
    def deposit(**kwargs):
        try:
            Transaction.objects.create(transaction_type=TransactionType.DEPOSIT, **kwargs)
        except Exception as e:
            logger.error(e)
            raise ModelNotCreatedException(e)

    @staticmethod
    def withdraw(**kwargs):
        try:
            Transaction.objects.create(transaction_type=TransactionType.WITHDRAWAL, **kwargs)
        except Exception as e:
            logger.error(e)
            raise ModelNotCreatedException(e)

    @staticmethod
    def transfer(**kwargs):
        try:
            Transaction.objects.create(transaction_type=TransactionType.TRANSFER, **kwargs)
        except Exception as e:
            logger.error(e)
            raise ModelNotCreatedException(e)
