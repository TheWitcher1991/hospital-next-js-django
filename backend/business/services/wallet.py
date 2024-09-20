from decimal import Decimal

from django.db import transaction
from rest_framework.generics import get_object_or_404

from patient.models import PatientBalance


class WalletService:
    """
    Сервис для работы с кошельком пациента
    """

    def __int__(self):
        pass

    @staticmethod
    def deposit(pk: int, amount: Decimal):
        with transaction.atomic():
            balance = get_object_or_404(PatientBalance.objects.select_for_update(), pk=pk)
            balance.balance += amount
            balance.save()
        return balance

    @staticmethod
    def withdraw(pk: int, amount: Decimal):
        with transaction.atomic():
            balance = get_object_or_404(PatientBalance.objects.select_for_update(), pk=pk)
            balance.balance -= amount
            balance.save()
        return balance
