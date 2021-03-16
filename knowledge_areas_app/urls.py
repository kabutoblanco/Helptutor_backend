from django.urls import path, include

from rest_framework import routers
from rest_framework.routers import DefaultRouter

from .api import *

router = DefaultRouter()
router.register('knowledgearea', KnowledgeAreaViewSet)
router.register('knowledgearea_tutor', KnowledgeArea_TutorViewSet)
router.register('knowledgeArea_student', KnowledgeArea_StudentViewSet)
router.register('cerficate', CerficateViewSet)
router.register('content', ContentViewSet)

urlpatterns = [
    path('api/', include(router.urls)),
]
