from django.urls import path
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from rest_framework_simplejwt.views import TokenObtainSlidingView, TokenRefreshSlidingView
from rest_framework import routers
from rest_framework.urlpatterns import format_suffix_patterns
from . import views

app_name = 'api'

# router = routers.SimpleRouter()

urlpatterns = [
    path('csrf/', views.csrfView, name='csrf'),
    path('services', views.ServiceTypeView.as_view(), name='service-type')
]

# urlpatterns += router

urlpatterns = format_suffix_patterns(urlpatterns)
