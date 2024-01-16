from rest_framework import serializers
from models.user import User
from models.patient import Patient, PatientPhone, PatientSignature, PatientType
from models.position import Position, Schedule, Shift, Cabinet
from models.employee import Employee
from models.service import ServiceType, Service
from models.patientcart import PatientCart
from models.agreement import Agreement, Talon


class UserSerializer(serializers.ModelSerializer):
    type = serializers.CharField(source='get_type_display')
    gender = serializers.CharField(source='get_gender_display')
    
    class Meta:
        model = User
        fields = '__all__'
        
        
class PatientTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = PatientType
        fields = '__all__'


class PatientSerializer(serializers.ModelSerializer):
    user = UserSerializer()
    patient_type = PatientTypeSerializer()
    
    class Meta:
        model = Patient
        fields = '__all__'


class PatientPhoneSerializer(serializers.ModelSerializer):
    patient = PatientSerializer()
    
    class Meta:
        model = PatientPhone
        fields = '__all__'


class PatientSignatureSerializer(serializers.ModelSerializer):
    patient = PatientSerializer()
    
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
    user = UserSerializer()
    cabinet = CabinetSerializer()
    position = PositionSerializer()
    
    class Meta:
        model = Employee
        fields = '__all__'


class ScheduleSerializer(serializers.ModelSerializer):
    shift = ShiftSerializer()
    employee = EmployeeSerializer()
    
    class Meta:
        model = Schedule
        fields = '__all__'
        

class ServiceTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = ServiceType
        fields = '__all__'
        

class ServiceSerializer(serializers.ModelSerializer):
    employee = EmployeeSerializer()
    service_type = ServiceTypeSerializer()
    
    class Meta:
        model = Service
        fields = '__all__'
        

class PatientCartSerializer(serializers.ModelSerializer):
    patient = PatientSerializer()
    service = ServiceSerializer()
    status = serializers.CharField(source='get_status_display')
    
    class Meta:
        model = PatientCart
        fields = '__all__'
       

class AgreementSerializer(serializers.ModelSerializer):
    patient_cart = PatientCartSerializer()

    class Meta:
        model = Agreement
        fields = '__all__'


class TalonSerializer(serializers.ModelSerializer):
    agreement = AgreementSerializer()

    class Meta:
        model = Talon
        fields = '__all__'
        