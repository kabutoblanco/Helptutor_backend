from django.urls import path, include

from rest_framework import routers
from rest_framework.routers import DefaultRouter

from .api import *

router = DefaultRouter()
router.register('schedule', ScheduleViewSet)
router.register('timeslot', TimeSlotViewSet)

urlpatterns = [
    path('api/', include(router.urls)),
]
