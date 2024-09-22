from datetime import datetime, timedelta
from decimal import Decimal

import jwt
from django.contrib.contenttypes.models import ContentType
from django.core.mail import send_mail
from django.db import transaction
from django.db.models import QuerySet
from django.utils import timezone
from num2words import num2words
from rest_framework.exceptions import AuthenticationFailed, NotFound, PermissionDenied, ValidationError

from config import settings

from .models import Session, User


def queryset_ids(queryset: QuerySet) -> list:
    return list(queryset.values_list("id", flat=True))


def get_content_type_for_model(model, for_concrete_model=True) -> ContentType:
    """
    Эта функция возвращает ContentType для модели
    """
    return ContentType.objects.get_for_model(model, for_concrete_model)


def mail(
    subject="next-hospital.com",
    message="",
    recipient="",
    fail_silently=False,
    **kwargs,
):
    send_mail(
        subject=subject,
        message=message,
        from_email="admin@next-hospital.com",
        recipient_list=[recipient],
        fail_silently=fail_silently,
        **kwargs,
    )


def jwt_encode(user, is_refresh=False) -> str:
    """
    Эта функция генерирует JSON Web Token (JWT) для заданного пользователя.
    """
    delta = (
        timedelta(days=settings.SESSION_EXPIRE_DAYS)
        if is_refresh
        else timedelta(minutes=settings.SESSION_EXPIRE_MINUTES)
    )

    dt = datetime.now() + delta
    exp_date = dt.strftime("%Y-%m-%d %H:%M:%S")
    token = jwt.encode(
        {
            "id": user.id,
            "email": user.email,
            "phone": user.phone,
            "first_name": user.first_name,
            "last_name": user.last_name,
            "is_staff": user.is_staff,
            "is_superuser": user.is_superuser,
            "role": user.role,
            "date_joined": user.date_joined.strftime("%Y-%m-%d %H:%M:%S"),
            "exp": dt.timestamp(),
            "exp_date": exp_date,
        },
        settings.SECRET_KEY,
        algorithm=settings.HASH_ALGORITHM,
    )
    return token


def jwt_decode(token) -> dict or None:
    """
    Декодировать JWT-токен
    """
    try:
        return jwt.decode(jwt=token, key=settings.SECRET_KEY, algorithms=[settings.HASH_ALGORITHM])
    except Exception as e:
        return False


def jwt_is_valid(token) -> bool:
    """
    Проверить, действителен ли JWT-токен
    """
    try:
        if not jwt_decode(token):
            return False

        decoded_token = jwt_decode(token)

        if not decoded_token:
            return False

        if decoded_token["exp"] < datetime.now().timestamp():
            return False
        return True
    except PermissionDenied as e:
        return False


def get_client_ip(request):
    x_forwarded_for = request.META.get("HTTP_X_FORWARDED_FOR")
    if x_forwarded_for:
        ip = x_forwarded_for.split(",")[0]
    else:
        ip = request.META.get("REMOTE_ADDR")
    return ip


def get_authorization_token(request):
    auth = request.headers.get("Authorization", b"")

    if not auth:
        return None

    try:
        return auth.split("Bearer ")[1]
    except IndexError:
        raise AuthenticationFailed('Invalid authorization header. Expected "Bearer <access_token>"')


def decimal_to_words(number) -> str:
    integer_part = int(number)
    fractional_part = int(round((number - integer_part) * 100))

    integer_part_words = num2words(integer_part, lang="ru")
    fractional_part_words = num2words(fractional_part, lang="ru")

    return f"{integer_part_words} рублей {fractional_part_words} копеек"


def discount_multiplier(discount: Decimal):
    return (100 - discount) / 100


def validate_email(email):
    if User.objects.filter(email=email).exists():
        raise ValidationError("Email is already in use")
    return email


def force_logout(request, user=None):
    from django.contrib.auth import logout

    try:
        auth = request.headers.get("Authorization", b"")
        token = auth.split("Bearer ")[1] if auth else None

        if not token:
            raise NotFound("Authorization token not provided")

        if user:
            sessions = Session.objects.filter(user=user)
        else:
            sessions = Session.objects.filter(user=request.user)

        with transaction.atomic():
            session_to_delete = sessions.filter(access_token=token).first()

            if not session_to_delete:
                raise NotFound("Session not found.")

            session_to_delete.user.last_ip = get_client_ip(request)
            session_to_delete.user.is_online = False
            session_to_delete.user.last_online = timezone.now()
            session_to_delete.user.save()

            session_to_delete.delete()

        logout(request)
    except Session.DoesNotExist:
        raise NotFound("Session not found.")
    except Exception as e:
        raise e
