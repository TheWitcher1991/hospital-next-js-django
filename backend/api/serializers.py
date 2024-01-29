from django.contrib.auth.password_validation import validate_password
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer, AuthUser
from rest_framework import serializers
from rest_framework_simplejwt.tokens import Token

from .models import *


class MyTokenObtainPairSerializer(TokenObtainPairSerializer):
    @classmethod
    def get_token(cls, user: AuthUser) -> Token:
        token = super().get_token(user)

        token['email'] = user.email
        token['first_name'] = user.first_name
        token['last_name'] = user.last_name
        token['patronymic'] = user.patronymic
        token['age'] = user.age
        token['date'] = user.date
        token['date_joined'] = user.date_joined
        token['role'] = user.role
        token['gender'] = user.gender

        return token


class UserCreateSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True, required=True, validators=[validate_password])

    class Meta:
        model = User
        fields = '__all__'

    def create(self, validated_data):
        user = User.objects.create(**validated_data)
        user.save()

        if user.role == 'П':
            patient = Patient.objects.create(user=user, **validated_data['patient'])
            patient.save()
        elif user.role == 'С':
            employee = Employee.objects.create(user=user, **validated_data['employee'])
            employee.save()

        return user


class UserSerializer(serializers.ModelSerializer):
    role = serializers.CharField(source='get_role_display')
    gender = serializers.CharField(source='get_gender_display')
    
    class Meta:
        model = User
        fields = '__all__'


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
        