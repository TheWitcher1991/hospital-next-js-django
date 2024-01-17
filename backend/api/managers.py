from django.db import models

from .models import *


class UserPatient(models.Manager):
    def get_queryset(self):
        return super().get_queryset().filter(type=User.Type.PATIENT)


class UserEmployee(models.Manager):
    def get_queryset(self):
        return super().get_queryset().filter(type=User.Type.EMPLOYEE)
    
    
class ServiceFreeManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset().filter(price=0)
    

class PatientCartDraftManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset().filter(status=PatientCart.Status.DRAFT)


class PatientCartActiveManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset().filter(status=PatientCart.Status.ACTIVE)


class PatientCartArchiveManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset().filter(status=PatientCart.Status.ARCHIVE)
    
    
class PatientCartWithOutDiagnoseManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset().filter(models.Q(diagnose='') | models.Q(diagnose__isnull=True))
    