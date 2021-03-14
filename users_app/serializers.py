from rest_framework import serializers

from users_app.models import Tutor


class TutorSerializer(serializers.ModelSerializer):
    password = serializers.CharField(min_length=4, write_only=True, required=True, style={'input_type': 'password'})

    class Meta:
        model = Tutor
        exclude = ['groups', 'user_permissions', ]

    def create(self, validated_data):
        instance = Tutor.objects.create(**validated_data)
        instance.set_password(validated_data.get('password'))
        instance.save()
        return instance

    
