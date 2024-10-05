from django.db import models
from django.utils.translation import gettext_lazy as _

from core.models import BaseModel

from .managers import ServiceFreeManager


class Employee(BaseModel):
    user = models.OneToOneField(to="core.User", on_delete=models.CASCADE, related_name="employee")
    cabinet = models.ForeignKey(to="core.Cabinet", on_delete=models.CASCADE, related_name="employees")
    position = models.ForeignKey(to="core.Position", on_delete=models.CASCADE, related_name="employees")

    class Meta:
        verbose_name = _("Сотрудник")
        verbose_name_plural = _("Сотрудники")

    def __str__(self):
        return f"{self.user} | {self.position}"


class Shift(BaseModel):
    number = models.CharField(_("Номер смены"), max_length=10)
    start = models.TimeField(_("Старт смены"))
    end = models.TimeField(_("Конец смены"))

    class Meta:
        verbose_name = _("Смена")
        verbose_name_plural = _("Смены")

    def __str__(self):
        return f"{self.number} | {self.start} - {self.end}"


class Schedule(BaseModel):
    date = models.DateField(_("Дата графика работы"))
    shift = models.ForeignKey(to=Shift, on_delete=models.CASCADE, related_name="schedules")
    employee = models.ForeignKey(to=Employee, on_delete=models.CASCADE, related_name="schedules")

    class Meta:
        verbose_name = _("График работы")
        verbose_name_plural = _("График работы")

    def __str__(self):
        return f"{self.date} | {self.employee} | {self.shift}"


class Service(BaseModel):
    name = models.CharField(_("Название"), max_length=128)
    price = models.DecimalField(_("Цена"), max_digits=10, decimal_places=2, default=0)
    employee = models.ForeignKey(to=Employee, on_delete=models.CASCADE, related_name="services")
    service_type = models.ForeignKey(to="core.ServiceType", on_delete=models.CASCADE, related_name="services")

    objects = models.Manager()
    free = ServiceFreeManager()

    class Meta:
        unique_together = ("name", "service_type")
        verbose_name = _("Услуга")
        verbose_name_plural = _("Услуги")

    def __str__(self):
        return f"{self.name} | {self.price} руб."
