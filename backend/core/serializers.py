from django.contrib.auth import authenticate
from django.contrib.auth.password_validation import validate_password
from django.db import transaction
from django.utils import timezone
from rest_framework import serializers
from rest_framework.exceptions import ValidationError

from config import settings

from .models import Cabinet, PatientType, Position, ServiceType, Session, User
from .utils import get_client_ip, jwt_encode


class SessionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Session
        fields = "__all__"
        read_only_fields = ("id", "created")


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
        from employee.models import Employee
        from patient.models import Patient

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

    class Meta:
        model = User
        fields = [
            "id",
            "email",
            "phone",
            "first_name",
            "last_name",
            "patronymic",
            "age",
            "date",
            "gender",
            "role",
            "date_joined",
            "updated_at",
            "is_active",
            "is_staff",
            "is_online",
            "last_online",
        ]
        read_only_fields = [
            "id",
            "created",
            "role",
            "email",
            "is_active",
            "is_staff",
            "is_online",
            "last_online",
        ]


class ServiceTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = ServiceType
        fields = "__all__"


class PatientTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = PatientType
        fields = "__all__"


class CabinetSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cabinet
        fields = "__all__"


class PositionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Position
        fields = "__all__"
