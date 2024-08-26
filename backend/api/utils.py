from datetime import timedelta, datetime

import jwt
from rest_framework.exceptions import AuthenticationFailed, PermissionDenied

from config import settings


def jwt_encode(user, is_refresh=False) -> str:
    """
    Эта функция генерирует JSON Web Token (JWT) для заданного пользователя.
    """
    delta = timedelta(days=settings.SESSION_EXPIRE_DAYS)\
        if is_refresh \
        else timedelta(minutes=settings.SESSION_EXPIRE_MINUTES)

    dt = datetime.now() + delta
    exp_date = dt.strftime('%Y-%m-%d %H:%M:%S')
    token = jwt.encode(
        {
            'id': user.id,
            'email': user.email,
            'phone': user.phone,
            'first_name': user.first_name,
            'last_name': user.last_name,
            'is_staff': user.is_staff,
            'is_superuser': user.is_superuser,
            'role': user.role,
            'date_joined': user.date_joined.strftime('%Y-%m-%d %H:%M:%S'),
            'exp': dt.timestamp(),
            'exp_date': exp_date,
        },
        settings.SECRET_KEY,
        algorithm=settings.HASH_ALGORITHM
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

        if decoded_token['exp'] < datetime.now().timestamp():
            return False
        return True
    except PermissionDenied as e:
        return False


def get_client_ip(request):
    x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
    if x_forwarded_for:
        ip = x_forwarded_for.split(',')[0]
    else:
        ip = request.META.get('REMOTE_ADDR')
    return ip


def get_authorization_token(request):
    auth = request.headers.get('Authorization', b'')

    if not auth:
        return None

    try:
        return auth.split('Bearer ')[1]
    except IndexError:
        raise AuthenticationFailed('Invalid authorization header. Expected "Bearer <access_token>"')