from django.contrib import admin

from .models import Cabinet, PatientType, Position, ServiceType, Session, User


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


@admin.register(Position)
class PositionAdmin(admin.ModelAdmin):
    list_display = ("name", "salary")
    search_fields = ("name",)


@admin.register(Cabinet)
class CabinetAdmin(admin.ModelAdmin):
    list_display = ("name", "number")
    search_fields = ("name", "number")


@admin.register(ServiceType)
class ServiceTypeAdmin(admin.ModelAdmin):
    list_display = ("name", "ico")
    search_fields = ("name",)
