"""Student api."""


# Django
from django.db import transaction

# rest_framework
from rest_framework import generics, status, viewsets, permissions, mixins
from rest_framework.decorators import action
from rest_framework.response import Response

# models
from helptutor.users.models import User, Student

# serializers
from helptutor.users.serializers import *

# permissions
from rest_framework.permissions import (
    AllowAny,
    IsAuthenticated
)

# utilities
from drf_yasg.utils import swagger_auto_schema
from utils.error import ValidationError


class StudentViewSet(mixins.CreateModelMixin,
                     mixins.UpdateModelMixin,
                     mixins.RetrieveModelMixin,
                     mixins.ListModelMixin,
                     viewsets.GenericViewSet):
    """Tutor view set."""

    queryset = Student.objects.filter(user__is_active=True)

    def get_permissions(self):
        """Assign permissions based on action."""
        if self.action in ['create']:
            permissions = [AllowAny]
        else:
            permissions = [IsAuthenticated]
        return [p() for p in permissions]

    def get_serializer_class(self):        
        """Return serializer based on action."""
        if self.action in ['create']:
            return StudentCreateSerializer
        return StudentViewSerializer

    @transaction.atomic
    @swagger_auto_schema(
        responses={status.HTTP_201_CREATED: StudentViewSerializer}
    )
    def create(self, request):
        if request.data.get('user', None):
            if request.data['user'].get('email', None):
                request.data['user']['username'] = request.data['user']['email']
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        student = serializer.save()
        data = StudentViewSerializer(student).data
        return Response(data, status=status.HTTP_201_CREATED)
    
    @swagger_auto_schema(
        request_body=StudentUpdateSerializer,
        responses={status.HTTP_200_OK: StudentViewSerializer}
    )
    @action(detail=False, methods=['patch'])
    def patch(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = StudentViewSerializer(instance, 
                                           data=request.data,
                                           partial=True)
        serializer.is_valid(raise_exception=True)
        student = serializer.save()
        serializer = UserUpdateSerializer(instance.user, 
                                          data=request.data['user'],
                                          partial=True)
        serializer.is_valid(raise_exception=True)
        user = serializer.save()
        data = StudentViewSerializer(student).data
        return Response(data, status=status.HTTP_200_OK)

    @swagger_auto_schema(
        responses={status.HTTP_200_OK: StudentViewSerializer}
    )
    @action(detail=False, methods=['get'], url_path='self')
    def get(self, request, *args, **kwargs):
        return super().retrieve(request)

    @swagger_auto_schema(
        responses={status.HTTP_200_OK: StudentViewSerializer}
    )
    @action(detail=True, methods=['get'])
    def get(self, request, *args, **kwargs):
        return super().retrieve(request)
    
    def get_object(self):
        try:
            return Student.objects.get(user=self.request.user.pk)
        except:
            raise ValidationError('Estudiante no existe')


class StudentBaseViewSet(mixins.UpdateModelMixin,
                         mixins.RetrieveModelMixin,
                         viewsets.GenericViewSet):
    """Tutor view set."""

    queryset = Student.objects.filter(user__is_active=True)

    def get_permissions(self):
        """Assign permissions based on action."""
        if self.action in ['create']:
            permissions = [AllowAny]
        else:
            permissions = [IsAuthenticated]
        return [p() for p in permissions]

    def get_serializer_class(self):        
        """Return serializer based on action."""
        if self.action in ['create']:
            return StudentCreateSerializer
        return StudentViewSerializer
    
    @swagger_auto_schema(
        request_body=StudentUpdateSerializer,
        responses={status.HTTP_200_OK: StudentViewSerializer}
    )
    def patch(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = StudentViewSerializer(instance,
                                           data=request.data,
                                           partial=True)
        serializer.is_valid(raise_exception=True)
        student = serializer.save()
        serializer = UserUpdateSerializer(instance.user, 
                                          data=request.data['user'],
                                          partial=True)
        serializer.is_valid(raise_exception=True)
        user = serializer.save()
        data = StudentViewSerializer(student).data
        return Response(data, status=status.HTTP_200_OK)

    def get_object(self):
        try:
            return Student.objects.get(user=self.kwargs['pk'])
        except:
            raise ValidationError('Estudiante no existe')
        

class StudentGoogleViewSet(mixins.CreateModelMixin,
                           viewsets.GenericViewSet):
    """StudentGoogle view set."""

    serializer_class = StudentGoogleCreateSerializer

    @swagger_auto_schema(
        responses={status.HTTP_201_CREATED: StudentViewSerializer}
    )
    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        tutor = serializer.save()
        data = StudentViewSerializer(tutor).data
        return Response(data, status=status.HTTP_200_OK)