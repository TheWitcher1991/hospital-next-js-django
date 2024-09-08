from core.defines import Role
from core.permissions import IsAuthenticated


class IsEmployee(IsAuthenticated):
    def has_permission(self, request, view):
        return request.user.role == Role.EMPLOYEE
