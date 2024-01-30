import json
from django.contrib.auth import authenticate, login, logout
from django.middleware.csrf import get_token
from django.core.exceptions import ObjectDoesNotExist
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import ensure_csrf_cookie
from rest_framework import generics
from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.authentication import SessionAuthentication

from .models import *
from .serializers import *
from .permissions import *


class MyTokenObtainPairView(TokenObtainPairView):
    serializer_class = MyTokenObtainPairSerializer


class CsrfView(APIView):
    permission_classes = (AllowAny, )
    authentication_classes = ()

    @method_decorator(ensure_csrf_cookie)
    def get(self, request):
        token = get_token(request)
        response = Response({'detail': token})
        response['X-CSRFToken'] = token
        return response


class LoginView(APIView):
    permission_classes = (AllowAny, )
    authentication_classes = ()

    def get(self, request):
        email = self.request.query_params.get('email')
        password = self.request.query_params.get('password')

        user = authenticate(email=email, password=password)

        if user is not None:
            login(request, user)
            serializer = UserSerializer(user)
            return Response(serializer.data)
        else:
            return Response(status=400)


class LogoutView(APIView):
    def post(self, request):
        logout(request)
        return Response({'detail': 'Successfully logged out.'})


class AuthenticateView(APIView):
    permission_classes = (AllowAny, )
    authentication_classes = ()

    @method_decorator(ensure_csrf_cookie)
    def get(self, request):
        if not request.user.is_authenticated:
            return Response({'isAuthenticated': False})

        return Response({'isAuthenticated': True})


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
