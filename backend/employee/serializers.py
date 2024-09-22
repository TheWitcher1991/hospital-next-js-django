from django.db import transaction
from rest_framework import serializers

from core.models import User
from core.serializers import CabinetSerializer, PositionSerializer, ServiceTypeSerializer, UserSerializer
from employee.models import Employee, Service


class EmployeeSerializer(serializers.ModelSerializer):
    user = UserSerializer(read_only=True)
    cabinet = CabinetSerializer()
    position = PositionSerializer()

    class Meta:
        model = Employee
        fields = "__all__"
        read_only_fields = ("id",)


class UpdateEmployeeSerializer(serializers.ModelSerializer):
    user = UserSerializer()

    class Meta:
        model = Employee
        fields = "__all__"
        read_only_fields = ("id",)

    def update(self, instance, validated_data):
        with transaction.atomic():
            user_data = validated_data.pop("user", {})

            instance = super().update(instance, validated_data)

            if user_data:
                user_instance = instance.user
                for key, value in user_data.items():
                    setattr(user_instance, key, value)
                user_instance.save()

            return instance


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
