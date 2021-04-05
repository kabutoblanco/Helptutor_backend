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

    @swagger_auto_schema(
        responses={status.HTTP_201_CREATED: LoginResponseSerializer}
    )
    def post(self, request, *args, **kwargs):
        response = super().create(request, args, kwargs)
        print(response)
        return response


class LoginGoogleAPI(mixins.CreateModelMixin, generics.GenericAPIView):
    """
    Retrieve a *jambalaya* recipe by name or country of origin
    """
    
    serializer_class = LoginGoogleSerializer

    @swagger_auto_schema(
        responses={status.HTTP_201_CREATED: LoginResponseSerializer}
    )
    def post(self, request, *args, **kwargs):
        return super().create(request, args, kwargs)