from django.contrib.auth import logout
from django.core.exceptions import ObjectDoesNotExist
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import ensure_csrf_cookie
from rest_framework.generics import GenericAPIView
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework.status import HTTP_200_OK, HTTP_403_FORBIDDEN, HTTP_404_NOT_FOUND
from rest_framework.views import APIView

from employee.serializers import ServiceSerializer

from .mixins import AllowAnyMixin
from .serializers import *


class LoginAPIView(GenericAPIView, AllowAnyMixin):

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

        serializer = self.serializer_class(
            data={"email": email, "password": password}, context={"request": self.request}
        )
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


class LogoutView(APIView):
    def post(self, request):
        logout(request)
        return Response({"detail": "Successfully logged out."})


class AuthenticateView(APIView):
    permission_classes = (AllowAny,)
    authentication_classes = ()

    @method_decorator(ensure_csrf_cookie)
    def get(self, request):
        if not request.user.is_authenticated:
            return Response({"isAuthenticated": False})

        return Response({"isAuthenticated": True})


class ServiceTypeListView(APIView):
    def get(self, request):
        serviceType = ServiceType.objects.all()
        serializer = ServiceTypeSerializer(serviceType, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = ServiceSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=404)


class ServiceTypeDetailView(APIView):
    def get_object(self, pk):
        try:
            return ServiceType.objects.get(pk=pk)
        except ObjectDoesNotExist:
            return Response(status=404)

    def get(self, request, pk):
        serviceType = self.get_object(pk)
        serializer = ServiceTypeSerializer(serviceType)
        return Response(serializer.data)

    def put(self, request, pk):
        serviceType = self.get_object(pk)
        serializer = ServiceTypeSerializer(serviceType, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=400)

    def delete(self, request, pk):
        serviceType = self.get_object(pk)
        serviceType.delete()
        return Response(status=204)


# class ServiceTypeView(generics.ListAPIView):
#     queryset = ServiceType.objects.all()
#     serializer_class = ServiceTypeSerializer
