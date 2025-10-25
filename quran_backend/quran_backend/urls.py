from django.urls import path, re_path
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from django.contrib import admin
from django.urls import include

schema_view = get_schema_view(
   openapi.Info(
      title="Admin API",
      default_version='v1',
      description="API for Admin Login",
      terms_of_service="https://example.com/terms/",
      contact=openapi.Contact(email="admin@example.com"),
   ),
   public=True,
   permission_classes=(permissions.AllowAny,),
)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('account/', include('account.urls')),
    path('adminuser/', include('adminuser.urls')),

    # Swagger UI at base URL
    path('', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),

    # Optional: JSON/YAML schema & ReDoc if needed
    re_path(r'^swagger(?P<format>\.json|\.yaml)$', schema_view.without_ui(cache_timeout=0), name='schema-json'),
    path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
]
