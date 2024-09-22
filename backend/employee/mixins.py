from functools import cached_property
from typing import TYPE_CHECKING

from django.db.models import QuerySet
from rest_framework.exceptions import NotFound
from rest_framework.generics import GenericAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.viewsets import ModelViewSet, ReadOnlyModelViewSet

from employee.models import Employee
from employee.permissions import IsEmployee

if TYPE_CHECKING:
    _ModelViewSet = ModelViewSet
    _ReadOnlyModelViewSet = ReadOnlyModelViewSet
    _GenericAPIView = GenericAPIView
else:
    _GenericAPIView = _ModelViewSet = _ReadOnlyModelViewSet = object


class EmployeeMixin:
    permission_classes = (IsEmployee,)
    employee_field: str = "employee_id"

    @cached_property
    def employee(self) -> Employee:
        try:
            return Employee.objects.get(user_id=self.request.user.id)
        except Employee.DoesNotExist:
            raise NotFound(detail="Employee not found")

    def get_queryset(self) -> QuerySet:
        try:
            if self.employee_field == "employee_id":
                return super().get_queryset().filter(employee_id=self.employee.id)
            else:
                return super().get_queryset().filter(**{self.employee_field: self.employee.id})
        except NotImplementedError:
            pass


class EmployeeViewMixin(EmployeeMixin, GenericAPIView):
    pass


class EmployeeControlViewMixin(EmployeeMixin, RetrieveUpdateDestroyAPIView):
    pass


class EmployeeViewSetMixin(EmployeeMixin, ModelViewSet):
    pass


class EmployeeReadOnlyViewSetMixin(EmployeeMixin, ReadOnlyModelViewSet):
    pass
