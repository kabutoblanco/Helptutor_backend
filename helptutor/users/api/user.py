# rest_framework
from rest_framework import generics, status, permissions, mixins
from rest_framework.authentication import BasicAuthentication
from rest_framework.response import Response

# models
from helptutor.users.models import User, Tutor

# serializers
from helptutor.users.serializers import *

# utilities
from drf_yasg.utils import swagger_auto_schema
from utils.error import ValidationError


class UserAPI(generics.RetrieveAPIView):
    permission_classes = [permissions.IsAuthenticated]

    serializer_class = UserViewSerializer

    def get_object(self):
        return self.request.user


class LoginAPI(mixins.CreateModelMixin, generics.GenericAPIView):
    serializer_class = LoginSerializer


class LoginGoogleAPI(mixins.CreateModelMixin, generics.GenericAPIView):
    serializer_class = LoginGoogleSerializer