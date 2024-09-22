from functools import cached_property
from typing import TYPE_CHECKING

from django.db.models import QuerySet
from rest_framework.exceptions import NotFound
from rest_framework.generics import GenericAPIView, ListCreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.viewsets import ModelViewSet, ReadOnlyModelViewSet

from patient.models import Patient
from patient.permissions import IsPatient

if TYPE_CHECKING:
    _ModelViewSet = ModelViewSet
    _ReadOnlyModelViewSet = ReadOnlyModelViewSet
    _GenericAPIView = GenericAPIView
else:
    _GenericAPIView = _ModelViewSet = _ReadOnlyModelViewSet = object


class PatientMixin:
    permission_classes = (IsPatient,)
    patient_field: str = "patient_id"

    @cached_property
    def patient(self) -> Patient:
        try:
            return Patient.objects.get(user_id=self.request.user.id)
        except Patient.DoesNotExist:
            raise NotFound(detail="Patient not found")

    def get_queryset(self) -> QuerySet:
        try:
            if self.patient_field == "patient_id":
                return super().get_queryset().filter(patient_id=self.patient.id)
            else:
                return super().get_queryset().filter(**{self.patient_field: self.patient.id})
        except NotImplementedError:
            pass


class PatientViewMixin(PatientMixin, GenericAPIView):
    pass


class PatientControlViewMixin(PatientMixin, RetrieveUpdateDestroyAPIView):
    pass


class PatientListenViewMixin(PatientMixin, ListCreateAPIView):
    pass


class PatientViewSetMixin(PatientMixin, ModelViewSet):
    pass


class PatientReadOnlyViewSetMixin(PatientMixin, ReadOnlyModelViewSet):
    pass
