from enum import Enum

from django.db import models
from django.utils.translation import gettext_lazy as _


class PaymentMethod(models.TextChoices):
    """
    Метод оплаты

    WARNING: Yookassa не работает с Balance и Cashless
    """
    CARD = 'bank_card', _('Банковская карта')
    SBERBANK = 'sberbank', _('SberPay')
    TINKOFF = 'tinkoff_bank', _('T‑Pay')
    SBP = 'sbp', _('СБП (Система быстрых платежей)')
    YOO_MONEY = 'yoo_money', _('ЮMoney')
    BALANCE = 'balance', _('С лицевого счета')
    CASHLESS = 'cashless', _('Безналичная оплата')


class YookassaVatCode(Enum):
    """
    Коды ставок НДС в Yookassa
    """
    without_vat = 1
    zero_vat = 2
    with_vat = 4


class YookassaSettlementsType(Enum):
    """
    Тип расчета в Yookassa
    """
    cashless = 'cashless',
    prepayment = 'prepayment',
    postpayment = 'postpayment',
    consideration = 'consideration',


class YookassaPaymentSubject(Enum):
    """
    Признак предмета расчета в Yookassa
    """
    commodity = 'commodity',
    job = 'job',
    service = 'service',
    payment = 'payment',
    another = 'another',


class YookassaPaymentMode(Enum):
    """
    Признак способа расчета в Yookassa
    """
    full_prepayment = 'full_prepayment',
    full_payment = 'full_payment',


class YookassaPaymentStatus(Enum):
    """
    Статус операции в Yookassa
    """
    pending = 'pending',
    waiting_for_capture = 'waiting_for_capture',
    succeeded = 'succeeded',
    canceled = 'canceled'


class YookassaPaymentCurrency(Enum):
    """
    Валюта операции в Yookassa
    """
    RUB = 'RUB',
    USD = 'USD'
