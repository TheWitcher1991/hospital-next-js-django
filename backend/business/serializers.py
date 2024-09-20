from rest_framework import serializers

from patient.models import PatientBalance
from patient.serializers import PatientSerializer

from .models import Invoice, Transaction


class YookassaWebhookSerializer(serializers.Serializer):
    type = serializers.CharField()
    event = serializers.CharField()
    object = serializers.DictField()


class InvoiceSerializer(serializers.ModelSerializer):
    patient = PatientSerializer(read_only=True)

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
