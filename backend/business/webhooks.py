import logging
from typing import Optional

from django.db import transaction
from django.utils import timezone
from rest_framework.exceptions import ParseError
from rest_framework.request import Request
from yookassa.domain.notification import PaymentWebhookNotification, WebhookNotificationEventType
from yookassa.domain.response import PaymentResponse

from .services.payment import PaymentService

logger = logging.getLogger("business")


class BusinessWebHook(object):
    """
    Сервис для обработки платежных оповещений от Yookassa
    """

    def __init__(self, request: Request) -> None:
        self.request: Request = request
        self.json: Optional[str] = None
        self.payment: Optional[PaymentResponse] = None
        self.webhook: Optional[PaymentWebhookNotification] = None

    def parse_json(self) -> None:
        try:
            logger.info(f"INFO: Получен объект webhook {self.request.data} | {timezone.now()}")
            self.json = self.request.data
        except Exception as e:
            logger.error(f"ERROR: Ошибка при получении json {e} | {timezone.now()}")
            raise ParseError(e)

    def receive_webhook_object(self) -> None:
        try:
            self.webhook = PaymentWebhookNotification(self.json)
            logger.info(f"INFO: Вызван объект webhook {self.webhook.event} | {timezone.now()}")
        except Exception as e:
            logger.error(f"ERROR: Ошибка при получении объекта webhook {e} | {timezone.now()}")
            raise ParseError(e)

    def get_payment(self) -> None:
        try:
            self.payment = PaymentService.find_one(self.webhook.object.id)
            logger.info(f"INFO: Получен объект payment {self.payment} | {timezone.now()}")
        except Exception as e:
            logger.error(f"ERROR: Ошибка при получении объекта payment {e} | {timezone.now()}")
            raise ParseError(e)

    def transport_webhook(self):
        logger.info(f"INFO: Передан webhook event {self.webhook.event} | {timezone.now()}")
        pass

    def execute(self) -> bool:
        with transaction.atomic():

            logger.info(f"INFO: Обработка завершена {self.payment.id} {self.webhook.event} | {timezone.now()}")

            return True
