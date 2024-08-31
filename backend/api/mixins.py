from rest_framework.permissions import AllowAny


class AllowAnyMixin:
    permission_classes = (AllowAny,)
    authentication_classes = ()
