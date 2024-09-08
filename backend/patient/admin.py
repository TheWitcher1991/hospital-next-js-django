from django.contrib import admin

from .models import Agreement, Patient, PatientCart, PatientPhone, PatientSignature, Talon


@admin.register(Patient)
class PatientAdmin(admin.ModelAdmin):
    list_display = ("user", "oms", "snils", "inn", "passport", "patient_type")
    search_fields = ("oms", "snils", "inn", "passport", "user__email")


@admin.register(PatientPhone)
class PatientPhoneAdmin(admin.ModelAdmin):
    list_display = ("patient", "phone")
    search_fields = ("phone", "patient__user__email")


@admin.register(PatientSignature)
class PatientSignatureAdmin(admin.ModelAdmin):
    list_display = ("patient", "signature")
    search_fields = ("signature", "patient__user__email")


@admin.register(PatientCart)
class PatientCartAdmin(admin.ModelAdmin):
    list_display = ("diagnose", "date_visit", "created", "status", "patient", "service")
    list_filter = ("status", "created", "date_visit")
    search_fields = ("patient__user__email", "service__name")


@admin.register(Agreement)
class AgreementAdmin(admin.ModelAdmin):
    list_display = ("start", "end", "patient_cart")
    list_filter = ("start", "end")
    search_fields = ("patient_cart__patient__user__email",)


@admin.register(Talon)
class TalonAdmin(admin.ModelAdmin):
    list_display = ("result", "agreement")
    search_fields = ("agreement__patient_cart__patient__user__email",)
