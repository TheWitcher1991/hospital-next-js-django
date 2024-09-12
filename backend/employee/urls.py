from django.urls import path

from . import views

app_name = "employee"

urlpatterns = [
    path("v1/services/", views.ServiceAPIView.as_view(), name="services"),
]
