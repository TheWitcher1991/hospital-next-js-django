from rest_framework.permissions import SAFE_METHODS, BasePermission
from rest_framework.permissions import IsAuthenticated as IsAuthenticatedDjango


class IsAuthenticated(IsAuthenticatedDjango):

    def has_permission(self, request, view):
        if not request.user.is_authenticated:
            return False
        return hasattr(request.user, "role")


class ReadOnly(BasePermission):
    def has_permission(self, request, view):
        return request.method in SAFE_METHODS
