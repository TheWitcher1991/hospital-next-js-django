import logging

from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
from rest_framework.generics import GenericAPIView
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework.status import HTTP_200_OK, HTTP_400_BAD_REQUEST

from api.mixins import AllowAnyMixin
from .serializers import YookassaWebhookSerializer
from .webhooks import BusinessWebHook

logger = logging.getLogger('business')


class YookassaWebhookView(GenericAPIView, AllowAnyMixin):
    """
    Обработка вебхука от yookassa
    """

    serializer_class = YookassaWebhookSerializer

    @method_decorator(csrf_exempt, name='dispatch')
    def post(self, request: Request, *args, **kwargs) -> Response:
        logger.info(f'WEBHOOK: IP address: {request.META.get('REMOTE_ADDR')} {request} {request.data}')
        webhook = BusinessWebHook(request=request)
        if webhook.execute():
            return Response({'detail': 'Подтверждение оплаты прошло успешно'}, status=HTTP_200_OK)
        else:
            return Response({'detail': 'Ошибка при обработке вебхука'}, status=HTTP_400_BAD_REQUEST)
