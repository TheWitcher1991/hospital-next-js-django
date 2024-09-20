from django_filters.rest_framework import FilterSet

from business.models import Invoice, Transaction


class InvoiceFilter(FilterSet):

    class Meta:
        model = Invoice
        fields = ("amount",)


class TransactionFilter(FilterSet):

    class Meta:
        model = Transaction
        fields = ("amount",)
