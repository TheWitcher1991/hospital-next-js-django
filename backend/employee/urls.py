from django.urls import path

from . import views

app_name = "employee"

urlpatterns = [
    path("v1/signup/employee/", views.SignupEmployeeAPIView.as_view(), name="signup-employee"),
    path("v1/services/", views.ServiceAPIView.as_view(), name="services"),
    path("v1/employee/", views.EmployeeAPIView.as_view(), name="employee"),
]
