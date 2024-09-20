import logging

from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
from rest_framework.generics import GenericAPIView, ListAPIView
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework.status import HTTP_200_OK, HTTP_400_BAD_REQUEST

from core.mixins import AllowAnyMixin
from patient.models import PatientBalance as Balance

from .filters import TransactionFilter
from .mixins import BusinessMixin
from .models import Transaction
from .serializers import BalanceSerializer, TransactionSerializer, YookassaWebhookSerializer
from .webhook import BusinessWebHook

logger = logging.getLogger("business")


class YookassaWebhookView(AllowAnyMixin, GenericAPIView):
    """
    Обработка вебхука от yookassa
    """

    serializer_class = YookassaWebhookSerializer

    @method_decorator(csrf_exempt, name="dispatch")
    def post(self, request: Request, *args, **kwargs) -> Response:
        logger.info(f"WEBHOOK: IP address: {request.META.get('REMOTE_ADDR')} {request} {request.data}")
        webhook = BusinessWebHook(request=request)
        if webhook.execute():
            return Response({"detail": "Подтверждение оплаты прошло успешно"}, status=HTTP_200_OK)
        else:
            return Response({"detail": "Ошибка при обработке вебхука"}, status=HTTP_400_BAD_REQUEST)


class BalanceAPIView(BusinessMixin, GenericAPIView):
    """
    Баланс пациента
    """

    queryset = Balance.objects.all()
    serializer_class = BalanceSerializer

    def get_queryset(self):
        return self.queryset.get(patient_id=self.request.user.patient.id)

    def get(self, request, *args, **kwargs):
        return Response(self.get_serializer(self.get_queryset()).data)


class TransactionListView(BusinessMixin, ListAPIView):
    """
    Список транзакций
    """

    queryset = Transaction.objects.all()
    filterset_class = TransactionFilter
    serializer_class = TransactionSerializer

    def get_queryset(self):
        return self.queryset.filter(patient_id=self.request.user.patient.id)
