from rest_framework import serializers
from backend.api.models.patient import PatientType, Patient, PatientPhone, PatientSignature


class PatientTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = PatientType
        fields = '__all__'


class PatientSerializer(serializers.ModelSerializer):
    class Meta:
        model = Patient
        fields = '__all__'


class PatientPhoneSerializer(serializers.ModelSerializer):
    class Meta:
        model = PatientPhone
        fields = '__all__'


class PatientSignatureSerializer(serializers.ModelSerializer):
    class Meta:
        model = PatientSignature
        fields = '__all__'
