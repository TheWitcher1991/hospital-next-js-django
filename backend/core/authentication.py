from django.contrib.auth.models import AnonymousUser
from django.utils.timezone import now
from rest_framework.authentication import BaseAuthentication, TokenAuthentication
from rest_framework.exceptions import AuthenticationFailed, PermissionDenied

from .models import Session
from .utils import force_logout, get_client_ip, jwt_is_valid


class SessionTokenAuthentication(TokenAuthentication):
    """
    Метод аутентификации для пользователей
    """

    def authenticate(self, request):
        try:
            auth = request.headers.get("Authorization", b"")

            if not auth:
                return None

            if isinstance(auth, bytes):
                auth = auth.decode("utf-8")

            try:
                token = auth.split("Bearer ")[1]
            except IndexError:
                raise PermissionDenied('Invalid authorization header. Expected "Bearer <access_token>"')

            if not token:
                return PermissionDenied("Access token is empty")

            if not jwt_is_valid(token):
                raise AuthenticationFailed("Access token not valid")

            session = Session.objects.filter(access_token=token).first()

            if not session:
                raise AuthenticationFailed("Session not found")

            if not jwt_is_valid(session.refresh_token):
                force_logout(request, user=session.user)
                request.user = AnonymousUser()
                raise AuthenticationFailed("Session has expired. Logout")

            request.user = session.user

            session.user.last_ip = get_client_ip(request)
            session.user.is_online = True
            session.user.last_online = now()
            session.user.save()

            return session.user, token
        except Session.DoesNotExist:
            raise PermissionDenied("Invalid token header. Token string should not contain invalid characters")


class RefreshTokenAuthentication(BaseAuthentication):
    """
    Метод аутентификации с использованием refresh_token
    """

    def authenticate(self, request):
        refresh_token = request.COOKIES["refresh_token"]

        if not refresh_token:
            return None

        try:
            session = Session.objects.filter(refresh_token=refresh_token).first()
            if not jwt_is_valid(refresh_token):
                force_logout(request)
                request.user = AnonymousUser()
                raise AuthenticationFailed("Session has expired. Logout")

            return session.user, None
        except Session.DoesNotExist:
            raise AuthenticationFailed("Invalid refresh token")
