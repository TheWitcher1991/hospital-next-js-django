from rest_framework import serializers

from employee.serializers import ServiceSerializer
from patient.models import PatientBalance
from patient.serializers import PatientSerializer

from .models import Invoice, InvoiceOrder, Transaction


class YookassaWebhookSerializer(serializers.Serializer):
    type = serializers.CharField()
    event = serializers.CharField()
    object = serializers.DictField()


class InvoiceOrderSerializer(serializers.Serializer):
    service = ServiceSerializer(read_only=True)

    class Meta:
        model = InvoiceOrder
        fields = "__all__"


class InvoiceSerializer(serializers.ModelSerializer):
    patient = PatientSerializer(read_only=True)
    services = InvoiceOrderSerializer(many=True, read_only=True)

    class Meta:
        model = Invoice
        fields = "__all__"


class CreateInvoiceOrderSerializer(serializers.Serializer):
    quantity = serializers.IntegerField()
    service_id = serializers.IntegerField()


class CreateInvoiceSerializer(serializers.ModelSerializer):
    services = CreateInvoiceOrderSerializer(many=True, required=True)

    class Meta:
        model = Invoice
        fields = "__all__"


class UpdateInvoiceSerializer(serializers.ModelSerializer):

    class Meta:
        model = Invoice
        fields = "__all__"


class TransactionSerializer(serializers.ModelSerializer):
    invoice = InvoiceSerializer(read_only=True)

    class Meta:
        model = Transaction
        fields = "__all__"


class BalanceSerializer(serializers.ModelSerializer):

    class Meta:
        model = PatientBalance
        fields = ("id", "balance")

    def save(self, **kwargs):
        pass
