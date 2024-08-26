from rest_framework.permissions import BasePermission, SAFE_METHODS, IsAuthenticated as IsAuthenticatedDjango

from api.defines import Role


class IsAuthenticated(IsAuthenticatedDjango):

    def has_permission(self, request, view):
        if not request.user.is_authenticated:
            return False
        return hasattr(request.user, 'role')


class ReadOnly(BasePermission):
    def has_permission(self, request, view):
        return request.method in SAFE_METHODS


class IsPatient(BasePermission):
    def has_permission(self, request, view):
        return request.user.role == Role.PATIENT
        

class IsEmployee(BasePermission):
    def has_permission(self, request, view):
        return request.user.role == Role.EMPLOYEE
    