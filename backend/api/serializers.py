from rest_framework import serializers
from .models import *


class UserSerializer(serializers.ModelSerializer):
    role = serializers.CharField(source='get_role_display')
    gender = serializers.CharField(source='get_gender_display')
    
    class Meta:
        model = User
        fields = '__all__'
        
    def create(self, validated_data):
        user = User.objects.create_user(**validated_data)
        return user


class PatientTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = PatientType
        fields = '__all__'


class PatientSerializer(serializers.ModelSerializer):
    user = UserSerializer(read_only=True)
    patient_type = PatientTypeSerializer(read_only=True)
    
    class Meta:
        model = Patient
        fields = '__all__'


class PatientPhoneSerializer(serializers.ModelSerializer):
    patient = PatientSerializer()
    
    class Meta:
        model = PatientPhone
        fields = '__all__'


class PatientSignatureSerializer(serializers.ModelSerializer):
    patient = PatientSerializer(read_only=True)
    
    class Meta:
        model = PatientSignature
        fields = '__all__'
        
        
class CabinetSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cabinet
        fields = '__all__'
        

class PositionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Position
        fields = '__all__'


class ShiftSerializer(serializers.ModelSerializer):
    class Meta:
        model = Shift
        fields = '__all__'
        

class EmployeeSerializer(serializers.ModelSerializer):
    user = UserSerializer(read_only=True)
    cabinet = CabinetSerializer(read_only=True)
    position = PositionSerializer(read_only=True)
    
    class Meta:
        model = Employee
        fields = '__all__'


class ScheduleSerializer(serializers.ModelSerializer):
    shift = ShiftSerializer(read_only=True)
    employee = EmployeeSerializer(read_only=True)
    
    class Meta:
        model = Schedule
        fields = '__all__'
        

class ServiceTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = ServiceType
        fields = '__all__'
        

class ServiceSerializer(serializers.ModelSerializer):
    employee = EmployeeSerializer(read_only=True)
    service_type = ServiceTypeSerializer(read_only=True)
    
    class Meta:
        model = Service
        fields = '__all__'
        

class PatientCartSerializer(serializers.ModelSerializer):
    patient = PatientSerializer(read_only=True)
    service = ServiceSerializer(read_only=True)
    status = serializers.CharField(source='get_status_display')
    
    class Meta:
        model = PatientCart
        fields = '__all__'
       

class AgreementSerializer(serializers.ModelSerializer):
    patient_cart = PatientCartSerializer(read_only=True)

    class Meta:
        model = Agreement
        fields = '__all__'


class TalonSerializer(serializers.ModelSerializer):
    agreement = AgreementSerializer(read_only=True)

    class Meta:
        model = Talon
        fields = '__all__'
        