
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
    path('', include('helptutor.advertisements.urls')),
    path('', include('helptutor.knowledge_areas.urls')),
    path('', include('helptutor.payments.urls')),
    path('', include('helptutor.places.urls')),
    path('', include('helptutor.schedules.urls')),
    path('', include('helptutor.services.urls')),
    path('', include('helptutor.sesions.urls')),
    path('', include('helptutor.users.urls')),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
