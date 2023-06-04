from drf_yasg import openapi
from drf_yasg.views import get_schema_view
from rest_framework import permissions
from django.urls import path, include


schema_view = get_schema_view(
    openapi.Info(
        title = "Auto library",
        default_version='v1',
        description="Магазин б/у комплектующих",
    ),
    public=True,
    permission_classes=(permissions.AllowAny,),
)

urlpatterns = [
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('redoc/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-redoc'),
    path('auth/', include('oauth.urls'))
]