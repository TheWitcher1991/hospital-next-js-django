from rest_framework.response import Response
from rest_framework.status import HTTP_201_CREATED

from core.mixins import CreateAllowAnyMixin

from .mixins import PatientReadOnlyViewSetMixin, PatientViewMixin, PatientViewSetMixin
from .models import Agreement, Patient, PatientCart, PatientPhone, PatientSignature, Talon
from .serializers import CreatePatientSerializer, UpdatePatientSerializer


class SignupPatientAPIView(CreateAllowAnyMixin):
    serializer_class = CreatePatientSerializer

    def create(self, *args, **kwargs) -> Response:
        serializer = self.get_serializer(data=self.request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        return Response({"ok": True}, status=HTTP_201_CREATED)


class PatientCartViewSet(PatientViewSetMixin):
    queryset = PatientCart.objects.all()


class PatientPhoneViewSet(PatientViewSetMixin):
    queryset = PatientPhone.objects.all()


class PatientSignatureViewSet(PatientViewSetMixin):
    queryset = PatientSignature.objects.all()


class PatientAgreementViewSet(PatientReadOnlyViewSetMixin):
    queryset = Agreement.objects.all()


class PatientTalonViewSet(PatientReadOnlyViewSetMixin):
    queryset = Talon.objects.all()


class PatientAPIView(PatientViewMixin):
    queryset = Patient.objects.all()
    serializer_class = UpdatePatientSerializer()

    def put(self, request, *args, **kwargs):
        partial = kwargs.pop("partial", False)
        serializer = self.get_serializer(instance=self.patient, data=request.data, partial=partial)
        serializer.is_valid(raise_exception=True)
        self.perform_update(serializer)
        return Response(serializer.data)

    def perform_update(self, serializer):
        serializer.save()

    def patch(self, request, *args, **kwargs):
        kwargs["partial"] = True
        return self.put(request, *args, **kwargs)
