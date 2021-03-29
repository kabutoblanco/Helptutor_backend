from rest_framework import serializers

from helptutor.users.models import Tutor
from .user import UserViewSerializer


class TutorSerializer(serializers.ModelSerializer):

    class Meta:
        model = Tutor
        fields = '__all__'

    
class TutorUpdateSerializer(serializers.ModelSerializer):

    class Meta:
        model = Tutor
        exclude = ('user', )

    
class TutorViewSerializer(serializers.ModelSerializer):
    user = UserViewSerializer()

    class Meta:
        model = Tutor
        fields = '__all__'