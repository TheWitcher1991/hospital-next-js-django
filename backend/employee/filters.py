from django_filters.rest_framework import FilterSet

from employee.models import Service


class ServiceFilter(FilterSet):
    class Meta:
        model = Service
        fields = ("employee", "service_type")
