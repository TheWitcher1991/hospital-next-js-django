from django.core.management.base import BaseCommand

from config.settings import (
    DJANGO_SUPERUSER_EMAIL,
    DJANGO_SUPERUSER_PASSWORD,
    DJANGO_SUPERUSER_PHONE,
    DJANGO_SUPERUSER_USERNAME,
)
from core.models import User


class Command(BaseCommand):

    def handle(self, *args, **options):
        username = DJANGO_SUPERUSER_USERNAME
        email = DJANGO_SUPERUSER_EMAIL
        phone = DJANGO_SUPERUSER_PHONE
        password = DJANGO_SUPERUSER_PASSWORD

        if not User.objects.filter(email=email).exists():
            print("Creating account for %s (%s)" % (username, email))
            User.objects.create_superuser(
                email=email,
                password=password,
                phone=phone,
                username=username,
            )
        else:
            print("Admin account has already been initialized.")
