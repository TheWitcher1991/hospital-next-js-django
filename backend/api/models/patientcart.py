from django.db import models
from patient import Patient
from service import Service


class PatientCartActiveManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset().filter(status=PatientCart.Status.ACTIVE)


class PatientCartArchiveManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset().filter(status=PatientCart.Status.ARCHIVE)


class PatientCartWithOutDiagnoseManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset().filter(models.Q(diagnose='') | models.Q(diagnose__isnull=True))


class PatientCart(models.Model):
    class Status(models.IntegerChoices):
        DRAFT = 0, 'Черновик'
        ACTIVE = 1, 'Обслуживание'
        ARCHIVE = 2, 'Архив'

    diagnose = models.CharField('Диагноз', max_length=256, blank=True, null=True)
    date_visit = models.DateField('Дата визита')
    created = models.DateTimeField('Дата', auto_now_add=True)
    status = models.SmallIntegerField('Статус', default=Status.DRAFT, choices=Status.choices)
    patient = models.ForeignKey(to=Patient, on_delete=models.CASCADE)
    service = models.ForeignKey(to=Service, on_delete=models.CASCADE)

    objects = models.Manager()
    actives = PatientCartActiveManager()
    archive = PatientCartArchiveManager()
    withOutDiagnose = PatientCartWithOutDiagnoseManager()

    class Meta:
        verbose_name = 'Амбулаторная карта'
        verbose_name_plural = 'Амбулаторные карты'
        ordering = ['-created']
        indexes = [
            models.Index(fields=['-created'])
        ]
