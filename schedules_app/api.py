from rest_framework import generics, viewsets
from rest_framework.response import Response
from rest_framework import status

from .models import (
    Schedule,
    TimeSlot,
)

from .serializers import (
    ScheduleSerializer,
    TimeSlotSerializer,
)

class ScheduleViewSet(viewsets.ModelViewSet):

    queryset = Schedule.objects.filter(is_active = True)
    serializer_class = ScheduleSerializer

class TimeSlotViewSet(viewsets.ModelViewSet):

    queryset = TimeSlot.objects.filter(is_active = True)
    serializer_class = TimeSlotSerializer
