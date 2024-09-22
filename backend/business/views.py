import logging

from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
from rest_framework.generics import GenericAPIView, ListAPIView
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework.status import HTTP_200_OK, HTTP_400_BAD_REQUEST

from core.mixins import AllowAnyMixin
from patient.mixins import PatientControlViewMixin, PatientListenViewMixin, PatientMixin, PatientViewMixin
from patient.models import PatientBalance as Balance

from .filters import InvoiceFilter, TransactionFilter
from .mixins import BusinessMixin
from .models import Invoice, Transaction
from .serializers import (
    BalanceSerializer,
    CreateInvoiceSerializer,
    InvoiceSerializer,
    TransactionSerializer,
    UpdateInvoiceSerializer,
    YookassaWebhookSerializer,
)
from .services.invoices import InvoiceService
from .services.transaction import TransactionService
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


class InvoiceAPIView(BusinessMixin, PatientListenViewMixin):
    """
    Список и создание счетов + yookassa
    """

    queryset = Invoice.objects.all()
    filterset_class = InvoiceFilter
    serializer_class = InvoiceSerializer

    def get_serializer_class(self):
        if self.request.method == "POST":
            return CreateInvoiceSerializer
        return super().get_serializer_class()

    def create(self, request, *args, **kwargs) -> Response:
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        invoice = InvoiceService().create(
            data={
                **request.data,
                "patient": self.patient,
            }
        )
        return Response({"confirmation_url": invoice.payment_url})


class InvoiceDetailAPIView(PatientControlViewMixin):
    queryset = Invoice.objects.all()
    serializer_class = InvoiceSerializer

    def get_serializer_class(self):
        if self.request.method in ["PUT", "PATCH"]:
            return UpdateInvoiceSerializer
        return super().get_serializer_class()


class TransactionListView(PatientMixin, BusinessMixin, ListAPIView):
    """
    Список транзакций
    """

    queryset = Transaction.objects.all()
    filterset_class = TransactionFilter
    serializer_class = TransactionSerializer


class TransactionStatsView(PatientViewMixin):
    """
    Статистика транзакций
    """

    queryset = Transaction.objects.all()
    serializer_class = TransactionSerializer

    def get(self, request, *args, **kwargs):
        return Response(
            {
                "total": TransactionService.count_all(patient_id=self.patient.id),
                "deposit": TransactionService.count_deposit(patient_id=self.patient.id),
                "withdrawal": TransactionService.count_withdrawal(patient_id=self.patient.id),
            }
        )
