from django.urls import path, include

from rest_framework import routers
from rest_framework.routers import DefaultRouter
from helptutor.users.api.user import *
from helptutor.users.api.tutor import *
from helptutor.users.api.student import *

from knox import views as knox_views


router = DefaultRouter()
router.register('tutor/google', TutorGoogleViewSet, basename='tutor_google')
router.register('tutor', TutorViewSet, basename='tutor')
router.register('base/tutor', TutorBaseViewSet, basename='base_tutor')
router.register('student/google', StudentGoogleViewSet, basename='student_google')
router.register('student', StudentViewSet, basename='student')
router.register('base/student', StudentBaseViewSet, basename='base_student')

urlpatterns = [
    # path('api/auth', include('knox.urls')),
    path('api/auth/user', UserAPI.as_view()),
    path('api/auth/login/google', LoginGoogleAPI.as_view()),
    path('api/auth/login', LoginAPI.as_view()),    
    path('api/auth/logout', knox_views.LogoutView.as_view(), name='knox_logout'),
    path('api/', include(router.urls)),
]
