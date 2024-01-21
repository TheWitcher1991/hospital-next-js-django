from rest_framework.permissions import BasePermission


class IsPatient(BasePermission):
    def has_permission(self, request, view):
        return request.user.role == 'П'
        

class IsEmployee(BasePermission):
    def has_permission(self, request, view):
        return request.user.role == 'С'
    