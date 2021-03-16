from django.urls import path, include

from rest_framework import routers
from rest_framework.routers import DefaultRouter

from .api import *

router = DefaultRouter()
router.register('KnowledgeArea', KnowledgeAreaViewSet)
router.register('KnowledgeArea_Tutor', KnowledgeArea_TutorViewSet)
router.register('KnowledgeArea_Student', KnowledgeArea_StudentViewSet)
router.register('Cerficate', CerficateViewSet)
router.register('Content', ContentViewSet)

urlpatterns = [
    path('api/', include(router.urls)),
]
