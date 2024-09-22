from rest_framework.response import Response
from rest_framework.status import HTTP_201_CREATED

from core.mixins import CreateAllowAnyMixin, ListEntityCacheMixin
from employee.filters import ServiceFilter
from employee.mixins import EmployeeControlViewMixin
from employee.models import Employee, Service
from employee.serializers import (
    CreateEmployeeSerializer,
    EmployeeSerializer,
    ServiceSerializer,
    UpdateEmployeeSerializer,
)


class SignupEmployeeAPIView(CreateAllowAnyMixin):
    serializer_class = CreateEmployeeSerializer

    def create(self, *args, **kwargs) -> Response:
        serializer = self.get_serializer(data=self.request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        return Response({"ok": True}, status=HTTP_201_CREATED)


class EmployeeAPIView(EmployeeControlViewMixin):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer
    employee_field = "id"

    def get_serializer_class(self):
        if self.request.method in ["PATCH", "PUT"]:
            return UpdateEmployeeSerializer
        return super().get_serializer_class()


class ServiceAPIView(ListEntityCacheMixin):
    queryset = Service.objects.all()
    serializer_class = ServiceSerializer
    filterset_class = ServiceFilter
    tag_cache = "service-list"
