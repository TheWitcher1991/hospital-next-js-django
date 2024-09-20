from patient.permissions import IsPatient


class BusinessMixin:
    permission_classes = (IsPatient,)
