from rest_framework import serializers

from users_app.models import Tutor


class TutorSerializer(serializers.ModelSerializer):
    password = serializers.CharField(min_length=4, write_only=True, required=True, style={'input_type': 'password'})

    class Meta:
        model = Tutor
        fields = '__all__'

    def create(self, validated_data):
        groups = validated_data.pop('groups')
        user_permissions = validated_data.pop('user_permissions')
        instance = Tutor.objects.create(**validated_data)
        instance.set_password(validate_data.get('password'))
        instance.user_permissions.set(user_permissions)
        instance.groups.set(groups)
        instance.save()
        return instance

    
