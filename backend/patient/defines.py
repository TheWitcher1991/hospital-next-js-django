from django.db import models
from django.utils.translation import gettext_lazy as _


class PatientCartStatus(models.TextChoices):
    DRAFT = "DRAFT", _("Черновик")
    ACTIVE = "ACTIVE", _("Обслуживание")
    ARCHIVE = "ARCHIVE", _("Архив")
