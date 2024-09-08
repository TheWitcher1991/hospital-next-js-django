from django.db.models.signals import post_save
from django.dispatch import receiver

from .models import Patient
from .tasks import create_patient_balance_task


@receiver(post_save, sender=Patient)
def create_patient_balance_signal(sender, instance: Patient, created, **kwargs):
    """
    Создание баланса пациента при регистрации
    """
    if created:
        create_patient_balance_task.delay(instance.id)
