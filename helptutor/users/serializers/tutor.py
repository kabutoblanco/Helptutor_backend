from rest_framework import serializers

from helptutor.users.models import User, Tutor
from .user import UserViewSerializer


class TutorSerializer(serializers.ModelSerializer):

    class Meta:
        model = Tutor
        fields = '__all__'

    def validate(self, data):
        """Validated user not is tutor."""
        tutor = Tutor.objects.filter(user=data['user'])
        if tutor.exists():
            raise serializers.ValidationError('Ya existe tutor')
        return data

    
class TutorUpdateSerializer(serializers.ModelSerializer):

    class Meta:
        model = Tutor
        exclude = ('user', )

    
class TutorViewSerializer(serializers.ModelSerializer):
    user = UserViewSerializer(read_only=True)

    class Meta:
        model = Tutor
        fields = '__all__'