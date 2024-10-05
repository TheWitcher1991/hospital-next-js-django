from django.db import transaction
from rest_framework import serializers

from core.defines import Role
from core.models import User
from core.serializers import PatientTypeSerializer, UserSerializer
from core.utils import get_client_ip
from patient.models import Agreement, Patient, PatientCart, PatientPhone, Talon


class PatientPhoneSerializer(serializers.ModelSerializer):
    class Meta:
        model = PatientPhone
        fields = "__all__"
        read_only_fields = ("id",)


class PatientSignatureSerializer(serializers.ModelSerializer):
    class Meta:
        model = PatientPhone
        fields = "__all__"
        read_only_fields = ("id",)


class PatientCartSerializer(serializers.ModelSerializer):
    class Meta:
        model = PatientCart
        fields = "__all__"
        read_only_fields = ("id",)


class TalonSerializer(serializers.ModelSerializer):
    class Meta:
        model = Talon
        fields = "__all__"
        read_only_fields = ("id",)


class AgreementSerializer(serializers.ModelSerializer):
    class Meta:
        model = Agreement
        fields = "__all__"
        read_only_fields = ("id",)


class PatientSerializer(serializers.ModelSerializer):
    user = UserSerializer(read_only=True)
    patient_type = PatientTypeSerializer(read_only=True)
    phones = PatientPhoneSerializer(many=True, read_only=True)

    class Meta:
        model = Patient
        fields = "__all__"
        read_only_fields = ("id",)


class OwnerPatientSerializer(PatientSerializer):
    signatures = PatientSignatureSerializer(many=True, read_only=True)


class UpdatePatientSerializer(serializers.ModelSerializer):
    user = UserSerializer()

    class Meta:
        model = Patient
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


class CreatePatientSerializer(serializers.ModelSerializer):
    oms = serializers.CharField(max_length=16, min_length=16, required=True)
    patient_type = serializers.PrimaryKeyRelatedField(read_only=True)

    class Meta:
        model = User
        fields = ("email", "password", "first_name", "last_name", "gender", "patronymic", "oms", "patient_type")
        extra_kwargs = {
            "email": {"required": True},
            "first_name": {"required": True},
            "last_name": {"required": True},
        }

    def create(self, validated_data):
        with transaction.atomic():
            user = User.objects.create(
                email=validated_data["email"],
                password=validated_data["password"],
                first_name=validated_data["first_name"],
                last_name=validated_data["last_name"],
                gender=validated_data["date"],
                patronymic=validated_data.get("patronymic", None),
                last_ip=get_client_ip(self.context["request"]),
                role=Role.PATIENT,
                is_active=True,
            )

            patient = Patient.objects.create(
                oms=validated_data["oms"], patient_type=validated_data["patient_type"], user=user
            )

            return patient
