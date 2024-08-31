from django.urls import path
from . import views

app_name = 'business'

urlpatterns = [
    path('v1/payments/webhooks/',
         views.YookassaWebhookView.as_view(),
         name='yookassa_webhook'),
]
