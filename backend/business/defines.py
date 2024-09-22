from django.db import models
from django.utils.translation import gettext_lazy as _


class PaymentMethod(models.TextChoices):
    """
    Метод оплаты

    WARNING: Yookassa не работает с Balance и Cashless
    """

    CARD = "bank_card", _("Банковская карта")
    SBERBANK = "sberbank", _("SberPay")
    TINKOFF = "tinkoff_bank", _("T‑Pay")
    SBP = "sbp", _("СБП (Система быстрых платежей)")
    YOO_MONEY = "yoo_money", _("ЮMoney")
    BALANCE = "balance", _("С лицевого счета")
    CASHLESS = "cashless", _("Безналичная оплата")


class InvoiceTarget(models.TextChoices):
    """
    Цель счета
    """

    BALANCE = "BALANCE", _("Пополнение баланса")
    SERVICE = "SERVICE", _("Оплата услуги")


class PayerType(models.TextChoices):
    """
    Тип плательщика
    """

    INDIVIDUAL = "INDIVIDUAL", _("Физическое лицо")
    LEGAL = "LEGAL", _("ЮЛ / ИП")


class TransactionType(models.TextChoices):
    """
    Тип операции
    """

    DEPOSIT = "DEPOSIT", _("Доход")
    WITHDRAWAL = "WITHDRAWAL", _("Расход")
    TRANSFER = "TRANSFER", _("Перевод средств")


class YookassaVatCode:
    """
    Коды ставок НДС в Yookassa
    """

    without_vat = 1
    zero_vat = 2
    with_vat = 4


class YookassaSettlementsType:
    """
    Тип расчета в Yookassa
    """

    cashless = "cashless"
    prepayment = "prepayment"
    postpayment = "postpayment"
    consideration = "consideration"


class YookassaPaymentSubject:
    """
    Признак предмета расчета в Yookassa
    """

    commodity = "commodity"
    job = "job"
    service = "service"
    payment = "payment"
    another = "another"


class YookassaPaymentMode:
    """
    Признак способа расчета в Yookassa
    """

    full_prepayment = "full_prepayment"
    full_payment = "full_payment"


class YookassaPaymentStatus:
    """
    Статус операции в Yookassa
    """

    pending = "pending"
    waiting_for_capture = "waiting_for_capture"
    succeeded = "succeeded"
    canceled = "canceled"


class YookassaPaymentCurrency:
    """
    Валюта операции в Yookassa
    """

    RUB = "RUB"
    USD = "USD"
