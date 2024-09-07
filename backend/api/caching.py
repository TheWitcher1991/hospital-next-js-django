from collections.abc import Iterable

from django.core.cache import cache
from django.db.models import Model, QuerySet
from rest_framework.generics import GenericAPIView
from rest_framework.mixins import (
    CreateModelMixin,
    DestroyModelMixin,
    ListModelMixin,
    RetrieveModelMixin,
    UpdateModelMixin,
)
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework.serializers import ModelSerializer


def clean_cache_by_tag(tag_cache: str) -> None:
    """
    Очищает кэш по тегу
    """
    keys = cache.keys(f"{tag_cache}*")
    cache.delete_many(keys)


def clean_group_cache_by_tags(tags_cache: Iterable[str]) -> None:
    """
    Очищает кэш по тегам
    """
    for tag_cache in tags_cache:
        clean_cache_by_tag(tag_cache)


class QuerysetCachedMixin(GenericAPIView):
    """
    Кэширование queryset
    """

    def get_queryset(self) -> QuerySet[Model]:
        key = f"{self.tag_cache}_queryset"
        queryset = cache.get(key)
        if not queryset:
            queryset = super().get_queryset()
            cache.set(key, queryset)
        return queryset


class ListCachedMixin(ListModelMixin):
    """
    Кэширование вывода списка
    """

    def list(self, request: Request, *args, **kwargs) -> Response:
        params = dict(sorted(request.GET.items())).__str__()
        key = f"{self.tag_cache}_queryset_{params}"
        data = cache.get(key)
        if not data:
            response = super().list(request, *args, **kwargs)
            cache.set(key, response.data)
            return response
        return Response(data)


class ListQuerysetCachedMixin(ListCachedMixin, QuerysetCachedMixin):
    """
    Кэширование вывода списка и queryset
    """


class ObjectCachedMixin(GenericAPIView):
    """
    Кеширование объекта
    """

    def get_object(self) -> Model:
        lookup = self.kwargs[self.lookup_field]
        key = f"{self.tag_cache}_object_{lookup}"
        obj = cache.get(key)
        if not obj:
            obj = super().get_object()
            cache.set(key, obj)
        return obj


class RetrieveCachedMixin(RetrieveModelMixin):
    """
    Кеширование вывода объекта
    """

    def retrieve(self, request: Request, *args, **kwargs) -> Response:
        lookup = self.kwargs[self.lookup_field]
        key = f"{self.tag_cache}_retrieve_{lookup}"
        data = cache.get(key)
        if not data:
            response = super().retrieve(request, *args, **kwargs)
            cache.set(key, response.data)
            return response
        return Response(data)


class RetrieveObjectCachedMixin(RetrieveCachedMixin, ObjectCachedMixin):
    """
    Кэширование вывода объекта и object
    """


class CleanCachedMixin:
    """
    Очистка кэша
    """

    def clean_cache(self, tag_cache: str) -> None:
        clean_cache_by_tag(tag_cache)

    def clean_group_cache(self, tags_cache: tuple[str]) -> None:
        clean_group_cache_by_tags(tags_cache)

    def clean_cache_update_destroy_object(
        self,
        tag_cache: str,
        lookup: str,
    ) -> None:
        tags_cache = (
            f"{tag_cache}_queryset",
            f"{tag_cache}_object_{lookup}",
            f"{tag_cache}_retrieve_{lookup}",
        )
        self.clean_group_cache(tags_cache)


class CreateCachedMixin(CreateModelMixin, CleanCachedMixin):
    """
    Очистка кэша при создании объекта"""

    def perform_create(self, serializer: ModelSerializer) -> None:
        super().perform_create(serializer)
        self.clean_cache(f"{self.tag_cache}_queryset")


class UpdateCachedMixin(UpdateModelMixin, CleanCachedMixin):
    """
    Очистка кэша при обновлении объекта
    """

    def perform_update(self, serializer: ModelSerializer) -> None:
        super().perform_update(serializer)
        lookup = self.kwargs[self.lookup_field]
        self.clean_cache_update_destroy_object(self.tag_cache, lookup)


class DestroyCachedMixin(DestroyModelMixin, CleanCachedMixin):
    """
    Очистка кэша при удалении объекта
    """

    def perform_destroy(self, instance: Model) -> None:
        super().perform_destroy(instance)
        lookup = self.kwargs[self.lookup_field]
        self.clean_cache_update_destroy_object(self.tag_cache, lookup)


class ListCreateCachedMixin(ListCachedMixin, CreateCachedMixin):
    """
    Кэширование списка данных и очистка при создании
    """


class CachedSetMixin(
    CreateCachedMixin,
    RetrieveCachedMixin,
    ObjectCachedMixin,
    UpdateCachedMixin,
    DestroyCachedMixin,
    ListCachedMixin,
    QuerysetCachedMixin,
):
    """
    Полный контроль кэширования
    """
