from core.mixins import ListEntityCacheMixin
from employee.models import Service
from employee.serializers import ServiceSerializer


class ServiceAPIView(ListEntityCacheMixin):
    queryset = Service.objects.all()
    serializer_class = ServiceSerializer
    tag_cache = "service-list"
