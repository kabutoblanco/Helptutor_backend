from django.urls import path, include

from rest_framework import routers
from rest_framework.routers import DefaultRouter
from users_app.api import *


router = DefaultRouter()
router.register('tutor', TutorViewSet)
router.register('google/tutor', TutorGoogleViewSet)

urlpatterns = [
    path('api/', include(router.urls)),
]
