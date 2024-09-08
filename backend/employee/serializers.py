from rest_framework import serializers

from core.serializers import ServiceTypeSerializer

from .models import Service


class ServiceSerializer(serializers.ModelSerializer):
    service_type = ServiceTypeSerializer(read_only=True)

    class Meta:
        model = Service
        fields = "__all__"
