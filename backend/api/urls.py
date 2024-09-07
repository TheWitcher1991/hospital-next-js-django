from django.urls import path

from . import views

app_name = "api"

urlpatterns = [
    path("v1/login/", views.LoginAPIView.as_view(), name="login"),
    path("v1/logout/", views.LogoutView.as_view(), name="logout"),
    path("v1/authenticate/", views.AuthenticateView.as_view(), name="authenticate"),
    path("v1/service-type/", views.ServiceTypeListView.as_view(), name="service-type"),
    path("v1/service-type/<int:pk>/", views.ServiceTypeDetailView.as_view(), name="service-type-pk"),
]
