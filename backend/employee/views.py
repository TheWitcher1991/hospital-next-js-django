from rest_framework.response import Response
from rest_framework.status import HTTP_201_CREATED

from core.mixins import CreateAllowAnyMixin, ListEntityCacheMixin
from employee.filters import ServiceFilter
from employee.models import Service
from employee.serializers import CreateEmployeeSerializer, ServiceSerializer


class SignupEmployeeAPIView(CreateAllowAnyMixin):
    serializer_class = CreateEmployeeSerializer

    def create(self, *args, **kwargs) -> Response:
        serializer = self.get_serializer(data=self.request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        return Response({"ok": True}, status=HTTP_201_CREATED)


class ServiceAPIView(ListEntityCacheMixin):
    queryset = Service.objects.all()
    serializer_class = ServiceSerializer
    filterset_class = ServiceFilter
    tag_cache = "service-list"
