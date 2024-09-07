from django.contrib import admin

from .models import (
    Agreement,
    Cabinet,
    Employee,
    Patient,
    PatientCart,
    PatientPhone,
    PatientSignature,
    PatientType,
    Position,
    Schedule,
    Service,
    ServiceType,
    Session,
    Shift,
    Talon,
    User,
)


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ("email", "first_name", "last_name", "role", "is_active", "is_staff")
    list_filter = ("is_active", "is_staff", "role", "gender", "date_joined")
    search_fields = ("email", "first_name", "last_name", "phone")
    ordering = ("-date_joined",)
    fieldsets = (
        (None, {"fields": ("email", "password")}),
        ("Personal info", {"fields": ("first_name", "last_name", "patronymic", "age", "date", "gender")}),
        ("Permissions", {"fields": ("is_active", "is_staff", "is_superuser", "groups", "user_permissions")}),
        ("Important dates", {"fields": ("last_login", "date_joined")}),
        ("Additional info", {"fields": ("phone", "role", "is_online", "last_ip", "last_online")}),
    )
    add_fieldsets = (
        (
            None,
            {
                "classes": ("wide",),
                "fields": ("email", "password1", "password2", "is_active", "is_staff", "is_superuser"),
            },
        ),
    )


@admin.register(Session)
class SessionAdmin(admin.ModelAdmin):
    list_display = ("user", "ip", "user_agent", "created", "expired")
    list_filter = ("created", "updated", "user__email")
    search_fields = ("ip", "user_agent", "user__email")
    ordering = ("-created",)


@admin.register(PatientType)
class PatientTypeAdmin(admin.ModelAdmin):
    list_display = ("name", "sale")
    search_fields = ("name",)


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


@admin.register(Position)
class PositionAdmin(admin.ModelAdmin):
    list_display = ("name", "salary")
    search_fields = ("name",)


@admin.register(Cabinet)
class CabinetAdmin(admin.ModelAdmin):
    list_display = ("name", "number")
    search_fields = ("name", "number")


@admin.register(Shift)
class ShiftAdmin(admin.ModelAdmin):
    list_display = ("number", "start", "end")
    search_fields = ("number",)


@admin.register(Employee)
class EmployeeAdmin(admin.ModelAdmin):
    list_display = ("user", "cabinet", "position")
    search_fields = ("user__email", "position__name", "cabinet__name")


@admin.register(Schedule)
class ScheduleAdmin(admin.ModelAdmin):
    list_display = ("date", "employee", "shift")
    list_filter = ("date", "shift")
    search_fields = ("employee__user__email",)


@admin.register(ServiceType)
class ServiceTypeAdmin(admin.ModelAdmin):
    list_display = ("name", "ico")
    search_fields = ("name",)


@admin.register(Service)
class ServiceAdmin(admin.ModelAdmin):
    list_display = ("name", "price", "employee", "service_type")
    list_filter = ("service_type",)
    search_fields = ("name", "employee__user__email")


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
