from rest_framework import serializers

from helptutor.services.models import Service


class ServiceModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Service
        fields = '__all__'


class ServiceCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Service
        exclude = ('tutor', )
