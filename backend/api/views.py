from django.http import JsonResponse
from django.views.decorators.csrf import ensure_csrf_cookie, csrf_protect
from django.views.decorators.http import require_POST
from rest_framework.decorators import api_view
from rest_framework import generics
from rest_framework.views import APIView

from .models import *
from .serializers import *


@ensure_csrf_cookie
def csrfView(request):
    return JsonResponse({'detail': 'CSRF cookie set'})


class ServiceTypeView(generics.ListAPIView):
    queryset = ServiceType.objects.all()
    serializers_class = ServiceTypeSerializer
    