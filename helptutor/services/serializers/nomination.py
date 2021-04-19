from rest_framework import serializers

from helptutor.services.models import Nomination


class NominationModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Nomination
        fields = '__all__'

class NominationCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Nomination
        fields = '__all__'