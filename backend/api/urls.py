from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from backend.api.views.patient import PatientList

urlpatterns = [
]

urlpatterns = format_suffix_patterns(urlpatterns)
