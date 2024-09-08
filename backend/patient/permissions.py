from core.defines import Role
from core.permissions import IsAuthenticated


class IsPatient(IsAuthenticated):
    def has_permission(self, request, view):
        return request.user.role == Role.PATIENT
