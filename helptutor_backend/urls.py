
from django.contrib import admin
from django.urls import path, include, re_path
from django.conf import settings
from django.conf.urls.static import static
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

schema_view = get_schema_view(
   openapi.Info(
      title="Documentación de API",
      default_version='v0.1',
      description="Documentación pública de API de Helptutor Backend",
      terms_of_service="https://www.google.com/policies/terms/",
      contact=openapi.Contact(email="tomasj@unicauca.edu.co"),
      license=openapi.License(name="BSD License"),
   ),
   public=True,
   permission_classes=(permissions.AllowAny,),
)

urlpatterns = [
    re_path(r'^swagger(?P<format>\.json|\.yaml)$', schema_view.without_ui(cache_timeout=0), name='schema-json'),
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
    path('admin/', admin.site.urls),
    path('', include('advertisements_app.urls')),
    path('', include('knowledge_areas_app.urls')),
    path('', include('payments_app.urls')),
    path('', include('places_app.urls')),
    path('', include('schedules_app.urls')),
    path('', include('services_app.urls')),
    path('', include('sesions_app.urls')),
    path('', include('users_app.urls')),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
