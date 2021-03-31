"""Tutor api."""


# rest_framework
from rest_framework import generics, status, viewsets, permissions, mixins
from rest_framework.decorators import action
from rest_framework.response import Response

# google services oauth
from google.oauth2 import id_token
from google.auth.transport import requests

# models
from helptutor.users.models import User, Tutor
from knox.models import AuthToken

# serializers
from helptutor.users.serializers import *

# permissions
from rest_framework.permissions import (
    AllowAny,
    IsAuthenticated
)

# utilities
from utils.error import ValidationError
from utils.string import get_random_string


class TutorViewSet(mixins.CreateModelMixin,
                   mixins.UpdateModelMixin,
                   mixins.RetrieveModelMixin,
                   mixins.ListModelMixin,
                   viewsets.GenericViewSet):
    """Tutor view set."""

    serializer_class = TutorSerializer
    queryset = Tutor.objects.filter(user__is_active=True)

    def get_permissions(self):
        """Assign permissions based on action."""
        if self.action in ['create']:
            permissions = [AllowAny]
        else:
            permissions = [IsAuthenticated]
        return [p() for p in permissions]

    def create(self, request):
        user = get_or_create_user(request)
        request.data['user'] = user.pk
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        tutor = serializer.save()
        data = TutorViewSerializer(tutor).data
        return Response(data, status=status.HTTP_201_CREATED)

    @action(detail=False, methods=['patch'], url_path="self")
    def self_update(self, request):
        self.serializer_class = TutorViewSerializer
        request.data['user'] = self.request.user.pk
        update_user(request, request.user.pk)
        return super().partial_update(request)

    def list(self, request):
        self.serializer_class = TutorViewSerializer
        return super().list(request)

    @self_update.mapping.get
    def self_retrieve(self, request):
        """Get tutor by pk to user."""
        self.serializer_class = TutorViewSerializer
        return super().retrieve(request)

    def get_object(self):
        try:
            return Tutor.objects.get(user=self.request.user.pk)
        except:
            raise ValidationError('Tutor no existe')
        

class TutorGoogleViewSet(mixins.CreateModelMixin,
                         viewsets.GenericViewSet):
    """TutorGoogle view set."""

    serializer_class = TutorSerializer
    queryset = Tutor.objects.all()

    def create(self, request, *args, **kwargs):
        token = request.data['id_token']
        CLIENT_ID = "581408483289-vlrheiceitim0evek4mrjnakqm5v07m7.apps.googleusercontent.com"
        try:
            idinfo = id_token.verify_oauth2_token(token, requests.Request(), CLIENT_ID)
            request = get_information_google(request, idinfo)
            user = get_or_create_user(request)
            request.data['user'] = user.pk
            serializer = self.get_serializer(data=request.data)
            serializer.is_valid(raise_exception=True)
            tutor = serializer.save()
        except ValueError:
            raise ValidationError('Error auth GoogleAPI')
        data = TutorViewSerializer(tutor).data
        return Response(data, status=status.HTTP_200_OK)


def get_or_create_user(request, *args, **kwargs):
    try:
        user = User.objects.get(email=request.data.get('email', None))
    except User.DoesNotExist:
        email = request.data.get('email', None)
        if email:
            request.data['username'] = email
        serializer = UserSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.save()
    return user


def update_user(request, pk, *args, **kwargs):
    try:
        user = User.objects.get(pk=pk)
        if request.data.get('password', None):
            user.set_password(request.data.pop('password'))
        serializer = UserUpdateSerializer(user, data=request.data, partial=True)
        serializer.is_valid(raise_exception=True)
        user = serializer.save()
    except User.DoesNotExist:
        pass


def get_information_google(request, idinfo, *args, **kwargs):
    userid = idinfo['sub']            
    request.data['first_name'] = idinfo['given_name']
    request.data['last_name'] = idinfo['family_name']
    request.data['email'] = idinfo['email']
    request.data['username'] = idinfo['email']
    request.data['password'] = get_random_string(8)
    return request