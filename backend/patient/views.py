from rest_framework.response import Response
from rest_framework.status import HTTP_201_CREATED

from core.mixins import CreateAllowAnyMixin

from .filters import AgreementFilter, PatientCartFilter, TalonFilter
from .mixins import PatientControlViewMixin, PatientReadOnlyViewSetMixin, PatientViewSetMixin
from .models import Agreement, Patient, PatientCart, PatientPhone, PatientSignature, Talon
from .serializers import (
    AgreementSerializer,
    CreatePatientSerializer,
    PatientPhoneSerializer,
    PatientSerializer,
    PatientSignatureSerializer,
    TalonSerializer,
    UpdatePatientSerializer,
)


class SignupPatientAPIView(CreateAllowAnyMixin):
    serializer_class = CreatePatientSerializer

    def create(self, *args, **kwargs) -> Response:
        serializer = self.get_serializer(data=self.request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        return Response({"ok": True}, status=HTTP_201_CREATED)


class PatientCartViewSet(PatientViewSetMixin):
    queryset = PatientCart.objects.all()
    serializer_class = PatientPhoneSerializer
    filterset_class = PatientCartFilter


class PatientPhoneViewSet(PatientViewSetMixin):
    queryset = PatientPhone.objects.all()
    serializer_class = PatientPhoneSerializer


class PatientSignatureViewSet(PatientViewSetMixin):
    queryset = PatientSignature.objects.all()
    serializer_class = PatientSignatureSerializer


class PatientAgreementViewSet(PatientReadOnlyViewSetMixin):
    queryset = Agreement.objects.all()
    serializer_class = AgreementSerializer
    filterset_class = AgreementFilter
    patient_field = "patient_cart__patient_id"


class PatientTalonViewSet(PatientReadOnlyViewSetMixin):
    queryset = Talon.objects.all()
    serializer_class = TalonSerializer
    filterset_class = TalonFilter
    patient_field = "agreement__patient_cart__patient_id"


class PatientAPIView(PatientControlViewMixin):
    queryset = Patient.objects.all()
    serializer_class = PatientSerializer
    patient_field = "id"

    def get_serializer_class(self):
        if self.request.method in ["PATCH", "PUT"]:
            return UpdatePatientSerializer
        return super().get_serializer_class()
