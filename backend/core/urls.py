from django.urls import path

from . import views

app_name = "core"

urlpatterns = [
    path("v1/login/", views.LoginAPIView.as_view(), name="login"),
    path("v1/logout/", views.LogoutAPIView.as_view(), name="logout"),
    path("v1/refresh/", views.RefreshTokenUpdateAPIView.as_view(), name="refresh-token"),
    path("v1/service-types/", views.ServiceTypeAPIView.as_view(), name="service-types"),
    path("v1/patient-types/", views.PatientTypeAPIView.as_view(), name="patient-types"),
    path("v1/cabinets/", views.CabinetAPIView.as_view(), name="cabinets"),
    path("v1/positions/", views.PositionAPIView.as_view(), name="positions"),
]
