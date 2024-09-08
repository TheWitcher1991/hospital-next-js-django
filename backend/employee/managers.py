from django.db import models


class ServiceFreeManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset().filter(price=0)
