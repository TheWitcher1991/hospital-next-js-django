from django.contrib import admin

from .models import Employee, Schedule, Service, Shift


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


@admin.register(Service)
class ServiceAdmin(admin.ModelAdmin):
    list_display = ("name", "price", "employee", "service_type")
    list_filter = ("service_type",)
    search_fields = ("name", "employee__user__email")
