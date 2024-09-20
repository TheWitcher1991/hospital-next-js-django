from django.urls import path

from . import views

app_name = "business"

urlpatterns = [
    path("v1/patient-balance/", views.BalanceAPIView.as_view(), name="patient-balance"),
    path(
        "v1/patient-transactions/",
        views.TransactionListView.as_view(),
        name="patient-transactions",
    ),
    path("v1/yookassa-webhook/", views.YookassaWebhookView.as_view(), name="yookassa-webhook"),
]
