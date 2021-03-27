from rest_framework import serializers
from django.contrib.auth import authenticate
from .models import User, Tutor


class LoginSerializer(serializers.Serializer):
    email = serializers.CharField()
    password = serializers.CharField()

    def validate(self, data):
        user = authenticate(**data)
        if user and user.is_active:
            return user
        raise serializers.ValidationError("Credenciales incorrectas")


class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        exclude = ('user_permissions', 'groups', )

    def create(self, validated_data):
        user = User.objects.create(**validated_data)
        user.set_password(validated_data['password'])
        user.save()
        return user


class UserUpdateSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        exclude = ('username', 'email', 'password', 'user_permissions', 'groups', )


class UserViewSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        exclude = ('password', )


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