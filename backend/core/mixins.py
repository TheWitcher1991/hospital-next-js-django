from django.utils.decorators import method_decorator
from django.views.decorators.cache import cache_page
from rest_framework.generics import CreateAPIView, GenericAPIView, ListAPIView
from rest_framework.permissions import AllowAny


class AllowAnyMixin:
    permission_classes = (AllowAny,)
    authentication_classes = ()


class GenericAllowAnyMixin(GenericAPIView, AllowAnyMixin):
    pass


class ListAllowAnyMixin(ListAPIView, AllowAnyMixin):
    pass


class CreateAllowAnyMixin(CreateAPIView, AllowAnyMixin):
    pass


class ListEntityCacheMixin(ListAllowAnyMixin):
    queryset = None
    serializer_class = None
    pagination_class = None
    tag_cache = None

    @method_decorator(cache_page(60 * 120, key_prefix=tag_cache))
    def get(self, request, *args, **kwargs):
        return super().get(request, *args, **kwargs)
