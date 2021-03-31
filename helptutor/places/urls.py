from django.urls import path, include

from rest_framework import routers
from rest_framework.routers import DefaultRouter

from .api import *


router = DefaultRouter()
router.register('country', CountryViewSet)
router.register('state', StateViewSet)
router.register('city', CityViewSet)
router.register('university', UniversityViewSet)

urlpatterns = [
    path('api/', include(router.urls)),
    path('api/country/<int:pk>/state/', CountryStatesAPIView.as_view()),
    path('api/state/<int:pk>/city/', StateCitiesAPIView.as_view()),
    path('api/city/<int:pk>/university/', CityUniversitiesAPIView.as_view())
]