from django.conf.urls.static import static
from django.contrib import admin
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.urls import include, path
from django.views.decorators.csrf import csrf_exempt
from drf_spectacular.views import SpectacularAPIView, SpectacularRedocView, SpectacularSwaggerView
from graphene_django.views import GraphQLView

from config import settings

app_name = "config"

urlpatterns = [
    path("api/admin/", admin.site.urls),
    path("api/", include("core.urls", namespace="core")),
    path("api/", include("patient.urls", namespace="patient")),
    path("api/", include("employee.urls", namespace="employee")),
    path("api/", include("business.urls", namespace="business")),
    path("graphql", csrf_exempt(GraphQLView.as_view(graphiql=settings.DEBUG))),
    path("gql", csrf_exempt(GraphQLView.as_view(batch=True))),
    path("v1/schema/", SpectacularAPIView.as_view(), name="schema"),
    path("v1/schema/swagger-ui/", SpectacularSwaggerView.as_view(url_name="schema"), name="swagger-ui"),
    path("v1/schema/redoc/", SpectacularRedocView.as_view(url_name="schema"), name="redoc"),
    path("", include("django_prometheus.urls")),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += staticfiles_urlpatterns()
    urlpatterns += [
        path("__debug__/", include("debug_toolbar.urls")),
    ]
