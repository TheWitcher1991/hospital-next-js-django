from functools import cached_property
from typing import TYPE_CHECKING

from django.db.models import QuerySet
from rest_framework.exceptions import NotFound
from rest_framework.generics import GenericAPIView
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

    @cached_property
    def patient(self) -> Patient:
        try:
            return Patient.objects.get(user_id=self.request.user.id)
        except Patient.DoesNotExist:
            raise NotFound(detail="Patient not found")

    def get_queryset(self) -> QuerySet:
        try:
            return super().get_queryset().filter(patient=self.patient)
        except NotImplementedError:
            pass


class PatientViewMixin(GenericAPIView, PatientMixin):
    pass


class PatientViewSetMixin(_ModelViewSet, PatientMixin):
    pass


class PatientReadOnlyViewSetMixin(_ReadOnlyModelViewSet, PatientMixin):
    pass
