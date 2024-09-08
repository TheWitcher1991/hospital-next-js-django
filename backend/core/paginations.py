from django.utils.translation import gettext_lazy as _
from rest_framework.pagination import LimitOffsetPagination, PageNumberPagination
from rest_framework.response import Response


class StandardLimitOffsetPagination(LimitOffsetPagination):
    """
    Базовый класс пагинации limit offset
    """

    limit_query_description = _("Количество результатов, возвращаемых на страницу")
    offset_query_description = _("Начальный индекс, по которому будут выводиться результаты")
    max_limit = 25
    default_limit = 25


class StandardPageNumberPagination(PageNumberPagination):
    """
    Базовый класс пагинации page number
    """

    page_query_description = _("Номер страницы в постраничном наборе результатов.")
    page_size_query_description = _("Количество результатов, возвращаемых на страницу")
    page_size = 25
    page_size_query_param = "page_size"
    max_page_size = 1000

    def get_paginated_response(self, data):
        return Response(
            {
                "count": self.page.paginator.count,
                "pages": self.page.paginator.num_pages,
                "next": self.get_next_link(),
                "previous": self.get_previous_link(),
                "results": data,
            }
        )
