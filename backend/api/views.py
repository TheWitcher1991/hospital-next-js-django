import json
from django.contrib.auth import authenticate, login
from django.http import JsonResponse
from django.middleware.csrf import get_token
from django.views.decorators.csrf import ensure_csrf_cookie
from rest_framework.decorators import api_view, permission_classes, authentication_classes
from rest_framework import generics
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.authentication import SessionAuthentication

from .models import *
from .serializers import *
from .permissions import *


class CsrfView(APIView):
    permission_classes = (AllowAny, )
    authentication_classes = ()

    @staticmethod
    def get(request):
        token = get_token(request)
        response = JsonResponse({'detail': token})
        response['X-CSRFToken'] = token
        return response


@api_view(['POST'])
@permission_classes([AllowAny])
def loginView(request):
    data = json.loads(request.body)
    email = data.get('email')
    password = data.get('password')

    user = authenticate(email=email, password=password)

    if user is not None:
        login(request, user)
        return Response({"detail": "Success"})


class ServiceTypeView(generics.ListAPIView):
    queryset = ServiceType.objects.all()
    serializer_class = ServiceTypeSerializer
