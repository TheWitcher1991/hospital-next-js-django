from django.db import models

from .defines import PatientCartStatus


class PatientCartDraftManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset().filter(status=PatientCartStatus.DRAFT)


class PatientCartActiveManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset().filter(status=PatientCartStatus.ACTIVE)


class PatientCartArchiveManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset().filter(status=PatientCartStatus.ARCHIVE)


class PatientCartWithOutDiagnoseManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset().filter(models.Q(diagnose="") | models.Q(diagnose__isnull=True))
