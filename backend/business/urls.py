from django.urls import path

from . import views

app_name = "business"

urlpatterns = [
    path("v1/patient-balance/", views.BalanceAPIView.as_view(), name="patient-balance"),
    path("v1/patient-invoices/", views.InvoiceAPIView.as_view(), name="patient-invoices"),
    path("v1/patient-invoices/<int:pk>/", views.InvoiceDetailAPIView.as_view(), name="patient-invoice-detail"),
    path(
        "v1/patient-transactions/",
        views.TransactionListView.as_view(),
        name="patient-transactions",
    ),
    path(
        "v1/patient-transactions/stats/",
        views.TransactionStatsView.as_view(),
        name="patient-transactions-stats",
    ),
    path("v1/yookassa-webhook/", views.YookassaWebhookView.as_view(), name="yookassa-webhook"),
]
