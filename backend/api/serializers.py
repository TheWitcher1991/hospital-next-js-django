from django.contrib.auth import authenticate
from django.contrib.auth.password_validation import validate_password
from django.db import transaction
from django.utils import timezone
from rest_framework import serializers
from rest_framework.exceptions import ValidationError

from config import settings

from .models import *
from .utils import get_client_ip, jwt_encode


class BaseLoginSerializer(serializers.Serializer):
    email = serializers.EmailField(required=True)
    password = serializers.CharField(required=True)
    access_token = serializers.CharField(read_only=True)
    expires = serializers.CharField(read_only=True)

    def to_representation(self, instance):
        representation = super().to_representation(instance)
        representation.pop("email", None)
        representation.pop("password", None)
        return representation

    @staticmethod
    def validate_session(user, request):
        ip = get_client_ip(request)

        session = Session.objects.create(
            user=user,
            access_token=jwt_encode(user, is_refresh=False),
            refresh_token=jwt_encode(user, is_refresh=True),
            refresh_token_expires=timezone.now() + timezone.timedelta(days=settings.SESSION_EXPIRE_DAYS),
            user_agent=request.META.get("HTTP_USER_AGENT"),
            ip=ip,
        )

        if not hasattr(user, "sessions"):
            Session.objects.filter(user=user).delete()
            raise ValidationError("Session not created")

        user.is_online = True
        user.last_ip = ip
        user.save()

        return session


class LoginSerializer(BaseLoginSerializer):
    account = serializers.JSONField(read_only=True)

    @staticmethod
    def get_user_data(user):
        try:
            return User.objects.get(user=user)
        except Exception as e:
            raise ValidationError(e)

    def validate(self, attrs):
        email = attrs.get("email", None)
        password = attrs.get("password", None)
        request = self.context["request"]

        if email is None:
            raise ValidationError("Email is required to login")
        if password is None:
            raise ValidationError("Password is required to login")

        user = authenticate(request, email=email, password=password)

        if user is None:
            raise ValidationError("Incorrect email or password")

        with transaction.atomic():
            session = self.validate_session(user, request)

            attrs["account"] = self.get_user_data(user)
            attrs["access_token"] = session.access_token
            attrs["expires"] = session.refresh_token_expires
            attrs["token_type"] = "Bearer"

            return attrs


class UserCreateSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True, required=True, validators=[validate_password])

    class Meta:
        model = User
        fields = "__all__"

    def create(self, validated_data):
        user = User.objects.create(**validated_data)
        user.save()

        if user.role == "П":
            patient = Patient.objects.create(user=user, **self.context["patient"])
            patient.save()
        elif user.role == "С":
            employee = Employee.objects.create(user=user, **self.context["employee"])
            employee.save()

        return user


class UserSerializer(serializers.ModelSerializer):
    role = serializers.CharField(source="get_role_display")
    gender = serializers.CharField(source="get_gender_display")
    password = serializers.CharField(read_only=True)

    class Meta:
        model = User
        fields = "__all__"


class PatientTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = PatientType
        fields = "__all__"


class PatientSerializer(serializers.ModelSerializer):
    user = UserSerializer(read_only=True)
    patient_type = PatientTypeSerializer(read_only=True)

    class Meta:
        model = Patient
        fields = "__all__"


class PatientPhoneSerializer(serializers.ModelSerializer):
    patient = PatientSerializer()

    class Meta:
        model = PatientPhone
        fields = "__all__"


class PatientSignatureSerializer(serializers.ModelSerializer):
    patient = PatientSerializer(read_only=True)

    class Meta:
        model = PatientSignature
        fields = "__all__"


class CabinetSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cabinet
        fields = "__all__"


class PositionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Position
        fields = "__all__"


class ShiftSerializer(serializers.ModelSerializer):
    class Meta:
        model = Shift
        fields = "__all__"


class EmployeeSerializer(serializers.ModelSerializer):
    user = UserSerializer(read_only=True)
    cabinet = CabinetSerializer(read_only=True)
    position = PositionSerializer(read_only=True)

    class Meta:
        model = Employee
        fields = "__all__"


class ScheduleSerializer(serializers.ModelSerializer):
    shift = ShiftSerializer(read_only=True)
    employee = EmployeeSerializer(read_only=True)

    class Meta:
        model = Schedule
        fields = "__all__"


class ServiceTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = ServiceType
        fields = "__all__"


class ServiceSerializer(serializers.ModelSerializer):
    employee = EmployeeSerializer(read_only=True)
    service_type = ServiceTypeSerializer(read_only=True)

    class Meta:
        model = Service
        fields = "__all__"


class PatientCartSerializer(serializers.ModelSerializer):
    patient = PatientSerializer(read_only=True)
    service = ServiceSerializer(read_only=True)
    status = serializers.CharField(source="get_status_display")

    class Meta:
        model = PatientCart
        fields = "__all__"


class AgreementSerializer(serializers.ModelSerializer):
    patient_cart = PatientCartSerializer(read_only=True)

    class Meta:
        model = Agreement
        fields = "__all__"


class TalonSerializer(serializers.ModelSerializer):
    agreement = AgreementSerializer(read_only=True)

    class Meta:
        model = Talon
        fields = "__all__"
