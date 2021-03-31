from rest_framework import serializers

from .models import (
    Schedule,
    TimeSlot,
)

class ScheduleSerializer(serializers.ModelSerializer):

    class Meta:
        model = Schedule
        fields = '__all__'

class TimeSlotSerializer(serializers.ModelSerializer):

    class Meta:
        model = TimeSlot
        fields = '__all__'
