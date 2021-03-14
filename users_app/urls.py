from django.urls import path, include

from rest_framework import routers
from rest_framework.routers import DefaultRouter
from users_app.api import TutorApi


router = DefaultRouter()
router.register('tutor', TutorApi)

urlpatterns = [
    path('api/', include(router.urls)),
]
