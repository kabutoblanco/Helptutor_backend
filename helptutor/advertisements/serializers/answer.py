from rest_framework import serializers

from helptutor.advertisements.models import Answer


class AnswerSerializer(serializers.ModelSerializer):

    class Meta:
        model = Answer
        fields = '__all__'