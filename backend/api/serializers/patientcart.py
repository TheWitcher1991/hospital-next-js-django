from rest_framework import serializers
from backend.api.models.patientcart import PatientCart


class PatientCartSerializer(serializers.ModelSerializer):
    class Meta:
        model = PatientCart
        fields = '__all__'
