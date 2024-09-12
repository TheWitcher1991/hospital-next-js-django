from django.urls import include, path
from rest_framework import routers

from . import views

app_name = "patient"

router = routers.SimpleRouter()

router.register(r"patient-carts", views.PatientCartViewSet)
router.register(r"patient-phones", views.PatientPhoneViewSet)
router.register(r"patient-signatures", views.PatientSignatureViewSet)
router.register(r"patient-agreements", views.PatientAgreementViewSet)
router.register(r"patient-talons", views.PatientTalonViewSet)

urlpatterns = [
    path("v1/signup/patient/", views.SignupPatientAPIView.as_view(), name="signup-patient"),
    path("v1/patient/", views.PatientAPIView.as_view(), name="patient"),
    path("v1/", include(router.urls)),
]
