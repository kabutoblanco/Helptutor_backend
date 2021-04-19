"""KnowledgeArea_Tutor view set."""


# rest_framework
from rest_framework import generics, status, viewsets
from rest_framework.response import Response

# models
from helptutor.knowledge_areas.models import KnowledgeArea_Tutor
from helptutor.users.models import Tutor
from helptutor.services.models import Service, Nomination
from helptutor.knowledge_areas.serializers import CertificateSerializer

# serializers
from helptutor.knowledge_areas.serializers import KnowledgeArea_TutorSerializer, KnowledgeArea_TutorViewSerializer

# utilities
from utils.error import ValidationError
import json


class KnowledgeArea_TutorViewSet(viewsets.ModelViewSet):
    """KnowledgeArea_Tutor view set."""

    serializer_class = KnowledgeArea_TutorSerializer
    queryset = KnowledgeArea_Tutor.objects.filter(is_active=True)

    def create(self, request, *args, **kwargs):
        request.body.decode('utf-8')
        print(request.data)
        request.data._mutable = True
        try:
            request.data['tutor'] = Tutor.objects.get(user=request.user.pk).pk
        except Tutor.DoesNotExist:
            raise ValidationError('Tutor no existe')
        print(request.data['certificate'])
        serializer = CertificateSerializer(data=request.data['certificate'])
        serializer.is_valid(raise_exception=True)
        instance = serializer.save()
        request.data._mutable = False
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        instance = serializer.save()
        data = KnowledgeArea_TutorViewSerializer(instance).data
        return Response(data, status=status.HTTP_201_CREATED)

    def partial_update(self, request, pk=None, **kwargs):
        context = self.get_serializer_context()
        context['action'] = 'patch'
        print(context)
        instance = self.get_object()
        serializer = self.get_serializer(instance, data=request.data, context=context, partial=True)
        serializer.is_valid(raise_exception=True)
        instance = serializer.save()
        data = KnowledgeArea_TutorViewSerializer(instance).data
        return Response(data, status=status.HTTP_200_OK)

    def destroy(self, request, pk=None):
        instance = self.get_object()
        instance.is_active = False
        self.perform_update(instance)
        Service.objects.filter(knowledgeArea_Tutor=instance.id).update(is_active=False)        
        if KnowledgeArea_Tutor.objects.filter(tutor=instance.tutor, is_active=True).exists() == False:
            Nomination.objects.filter(tutor=instance.tutor).update(is_active=False)
        return Response(status=status.HTTP_200_OK)


class TutorSpecialitiesAPIList(generics.ListAPIView):

    queryset = KnowledgeArea_Tutor.objects.all()
    serializer_class = KnowledgeArea_TutorViewSerializer

    def list(self, request, *args, **kwargs):
        #pk: corresponde al id del tutor
        queryset = KnowledgeArea_Tutor.objects.filter(tutor__user=kwargs['pk'], is_active=True)
        data = self.get_serializer(queryset, many=True).data
        return Response(data, status=status.HTTP_200_OK)