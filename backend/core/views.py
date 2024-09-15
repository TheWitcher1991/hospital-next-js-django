from django.contrib.auth.models import AnonymousUser
from rest_framework.exceptions import NotFound
from rest_framework.generics import GenericAPIView
from rest_framework.response import Response
from rest_framework.status import (
    HTTP_200_OK,
    HTTP_400_BAD_REQUEST,
    HTTP_401_UNAUTHORIZED,
    HTTP_403_FORBIDDEN,
    HTTP_404_NOT_FOUND,
)

from config import settings

from .authentication import RefreshTokenAuthentication
from .filters import CabinetFilter, ServiceTypeFilter
from .mixins import GenericAllowAnyMixin, ListEntityCacheMixin
from .models import Cabinet, PatientType, Position, ServiceType, Session, User
from .permissions import IsAuthenticated
from .serializers import (
    CabinetSerializer,
    LoginSerializer,
    PatientTypeSerializer,
    PositionSerializer,
    ServiceTypeSerializer,
    SessionSerializer,
)
from .utils import force_logout, jwt_encode, jwt_is_valid


class LoginAPIView(GenericAllowAnyMixin):

    queryset = User.objects.all()
    serializer_class = LoginSerializer

    def post(self, *args, **kwargs) -> Response:
        email = self.request.data.get("email")
        password = self.request.data.get("password")

        user = self.queryset.get(email=email)

        if user is None:
            return Response({"msg": "user not found"}, status=HTTP_404_NOT_FOUND)

        if user.is_staff or user.is_superuser:
            return Response({"msg": "user is not an employer"}, status=HTTP_403_FORBIDDEN)

        serializer = self.get_serializer(data={"email": email, "password": password}, context={"request": self.request})
        serializer.is_valid(raise_exception=True)

        refresh_token = serializer.data.pop("refresh_token", None)

        response = Response(serializer.data, status=HTTP_200_OK)

        response.set_cookie(
            "refresh_token",
            refresh_token,
            httponly=True,
            secure=True,
            samesite="Strict",
            expires=settings.SESSION_EXPIRE_DAYS * 24 * 60 * 60,
        )

        return response


class RefreshTokenUpdateAPIView(GenericAPIView):
    """
    Получение нового токена авторизации
    """

    queryset = Session.objects.all()
    serializer_class = SessionSerializer
    permission_classes = (IsAuthenticated,)
    authentication_classes = (RefreshTokenAuthentication,)

    def put(self, request, *args, **kwargs):
        refresh_token = request.COOKIES["refresh_token"]

        if not refresh_token:
            return Response({"msg": "Refresh token is required"}, status=HTTP_400_BAD_REQUEST)

        try:
            session = self.queryset.filter(refresh_token=refresh_token).first()
        except Session.DoesNotExist:
            return Response({"msg": "Invalid refresh token"}, status=HTTP_401_UNAUTHORIZED)

        if not jwt_is_valid(refresh_token):
            force_logout(request)
            request.user = AnonymousUser()
            return Response({"msg": "Session has expired. Logout"}, status=HTTP_401_UNAUTHORIZED)

        access_token = jwt_encode(session.user, is_refresh=False)
        session.access_token = access_token
        session.save()

        return Response(
            {
                "access_token": access_token,
            },
            status=HTTP_200_OK,
        )


class LogoutAPIView(GenericAPIView):
    permission_classes = (IsAuthenticated,)

    def post(self, request, *args, **kwargs) -> Response:
        try:
            force_logout(self.request)
            return Response({"isAuthenticated": False}, status=HTTP_200_OK)
        except NotFound as e:
            return Response({"detail": str(e)}, status=HTTP_400_BAD_REQUEST)
        except Exception as e:
            return Response({"detail": "An unexpected error occurred."}, status=HTTP_400_BAD_REQUEST)


class ServiceTypeAPIView(ListEntityCacheMixin):
    queryset = ServiceType.objects.all()
    serializer_class = ServiceTypeSerializer
    filterset_class = ServiceTypeFilter
    tag_cache = "service-type-list"


class PatientTypeAPIView(ListEntityCacheMixin):
    queryset = PatientType.objects.all()
    serializer_class = PatientTypeSerializer
    tag_cache = "patient-type-list"


class CabinetAPIView(ListEntityCacheMixin):
    queryset = Cabinet.objects.all()
    serializer_class = CabinetSerializer
    filterset_class = CabinetFilter
    tag_cache = "cabinet-type-list"


class PositionAPIView(ListEntityCacheMixin):
    queryset = Position.objects.all()
    serializer_class = PositionSerializer
    tag_cache = "position-list"
