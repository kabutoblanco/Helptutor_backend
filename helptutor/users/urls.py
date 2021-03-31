from django.urls import path, include

from rest_framework import routers
from rest_framework.routers import DefaultRouter
from helptutor.users.api.user import *
from helptutor.users.api.tutor import *

from knox import views as knox_views


router = DefaultRouter()
router.register('tutor', TutorViewSet, basename='tutor')
router.register('google/tutor', TutorGoogleViewSet, basename='tutor-google')

urlpatterns = [
    path('api/auth', include('knox.urls')),
    path('api/auth/user', UserAPI.as_view()),
    path('api/auth/login', LoginAPI.as_view()),
    path('api/auth/google/login', LoginGoogleAPI.as_view()),
    path('api/auth/logout', knox_views.LogoutView.as_view(), name='knox_logout'),
    path('api/', include(router.urls)),
]
