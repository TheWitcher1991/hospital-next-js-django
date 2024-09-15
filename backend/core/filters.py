from django_filters.rest_framework import FilterSet

from core.models import Cabinet, ServiceType


class CabinetFilter(FilterSet):
    class Meta:
        model = Cabinet
        fields = ("number",)


class ServiceTypeFilter(FilterSet):
    class Meta:
        model = ServiceType
        fields = ("name",)
