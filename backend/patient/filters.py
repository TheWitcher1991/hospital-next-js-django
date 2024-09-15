from django_filters.rest_framework import FilterSet

from patient.models import Agreement, PatientCart, Talon


class PatientCartFilter(FilterSet):
    class Meta:
        model = PatientCart
        fields = ("service", "patient")


class AgreementFilter(FilterSet):
    class Meta:
        model = Agreement
        fields = ("patient_cart",)


class TalonFilter(FilterSet):
    class Meta:
        model = Talon
        fields = ("agreement",)
