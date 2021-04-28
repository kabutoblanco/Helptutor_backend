from rest_framework import serializers

from helptutor.advertisements.models import Answer


class AnswerSerializer(serializers.ModelSerializer):

    class Meta:
        model = Answer
        fields = '__all__'

    def to_representation(self, instance):
        return {
            'id':instance.id,
            'likes':instance.likes,
            'description':instance.description,
            'advertisement':instance.advertisement.title,
            'user':instance.user.first_name
        }
