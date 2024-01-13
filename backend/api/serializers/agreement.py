from rest_framework import serializers
from backend.api.models.agreement import Agreement, Talon


class AgreementSerializer(serializers.ModelSerializer):
    class Meta:
        model = Agreement
        fields = '__all__'


class TalonSerializer(serializers.ModelSerializer):
    class Meta:
        model = Talon
        fields = '__all__'
