from django.urls import path
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from rest_framework_simplejwt.views import TokenObtainSlidingView, TokenRefreshSlidingView
from rest_framework.urlpatterns import format_suffix_patterns

urlpatterns = [

]

urlpatterns = format_suffix_patterns(urlpatterns)
