from rest_framework import serializers

from core.models import User
from core.serializers import ServiceTypeSerializer
from employee.models import Service


class CreateEmployeeSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = (
            "email",
            "password",
            "first_name",
            "last_name",
            "gender",
            "patronymic",
        )
        extra_kwargs = {
            "email": {"required": True},
            "first_name": {"required": True},
            "last_name": {"required": True},
        }


class ServiceSerializer(serializers.ModelSerializer):
    service_type = ServiceTypeSerializer(read_only=True)

    class Meta:
        model = Service
        fields = "__all__"
