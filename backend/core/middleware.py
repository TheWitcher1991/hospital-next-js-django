from django.contrib.auth.models import AnonymousUser
from django.http import HttpResponseForbidden
from rest_framework.exceptions import AuthenticationFailed, PermissionDenied

from .authentication import SessionTokenAuthentication
from .defines import Role
from .models import User
from .utils import get_client_ip


class TokenMiddleware:
    """
    Middleware, чтобы проверить токен
    """

    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        if request.user.is_authenticated:
            if request.user.is_superuser or request.user.is_staff:
                return self.get_response(request)

            try:
                user, token = SessionTokenAuthentication().authenticate(request)

                if user:
                    request.user = user
            except (PermissionDenied, AuthenticationFailed) as e:
                return PermissionDenied(e)
        else:
            request.user = AnonymousUser()

        return self.get_response(request)


class PingUserMiddleware:
    """
    Middleware, чтобы проверить, активен ли пользователь
    """

    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        if request.user.is_authenticated and hasattr(request.user, "role"):
            current_user = request.user.id
            try:
                user = User.objects.get(id=current_user)

                if not user.is_staff or not user.is_superuser:
                    user.is_online = True

                user.last_ip = get_client_ip(request)
                user.save()
            except User.DoesNotExist:
                raise HttpResponseForbidden
        else:
            request.user.role = Role.GUEST
        return self.get_response(request)
