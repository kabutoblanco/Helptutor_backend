from django.urls import path, include
 
from rest_framework import routers
from rest_framework.routers import DefaultRouter

from helptutor.knowledge_areas.api import *

router = DefaultRouter()
router.register('knowledgearea', KnowledgeAreaViewSet)
router.register('knowledgearea_tutor', KnowledgeArea_TutorViewSet)
router.register('knowledgearea_student', KnowledgeArea_StudentViewSet)
router.register('certificate', CertificateViewSet)
router.register('content', ContentViewSet)

urlpatterns = [
    path('api/', include(router.urls)),
    path('api/knowledgearea/<int:pk>/knowledgearea/', KnowledgeAreaCategoryAPIView.as_view()),
    path('api/tutor/<int:pk>/speciality/', TutorSpecialitiesAPIList.as_view()),
]
