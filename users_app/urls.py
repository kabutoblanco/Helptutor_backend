from django.urls import path, include

from rest_framework import routers
from rest_framework.routers import DefaultRouter
from users_app.api import *

from knox import views as knox_views


router = DefaultRouter()
router.register('tutor', TutorViewSet)
router.register('google/tutor', TutorGoogleViewSet)

urlpatterns = [
    path('api/auth', include('knox.urls')),
    path('api/auth/user', UserAPI.as_view()),
    path('api/auth/login', LoginAPI.as_view()),
    path('api/auth/logout', knox_views.LogoutView.as_view(), name='knox_logout'),
    path('api/', include(router.urls)),
]
