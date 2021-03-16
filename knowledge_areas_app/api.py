from rest_framework import generics, viewsets
from rest_framework.response import Response
from rest_framework import status
from .serializers import (
    KnowledgeAreaSerializer,
    KnowledgeArea_TutorSerializer,
    KnowledgeArea_StudentSerializer,
    CerficateSerializer,
    ContentSerializer
)
from .models import (
    KnowledgeArea,
    KnowledgeArea_Tutor,
    KnowledgeArea_Student,
    Cerficate,
    Content,
)

class KnowledgeAreaViewSet(viewsets.ModelViewSet):

    queryset = KnowledgeArea.objects.filter(is_active = True)
    serializer_class = KnowledgeAreaSerializer

    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        instance.is_active = False
        self.perform_update(instance)
        return Response(status=status.HTTP_204_NO_CONTENT)

class KnowledgeArea_TutorViewSet(viewsets.ModelViewSet):

    queryset = KnowledgeArea_Tutor.objects.filter(is_active = True)
    serializer_class = KnowledgeArea_TutorSerializer

    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        instance.is_active = False
        self.perform_update(instance)
        return Response(status=status.HTTP_204_NO_CONTENT)

class KnowledgeArea_StudentViewSet(viewsets.ModelViewSet):

    queryset = KnowledgeArea_Student.objects.filter(is_active = True)
    serializer_class = KnowledgeArea_StudentSerializer

    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        instance.is_active = False
        self.perform_update(instance)
        return Response(status=status.HTTP_204_NO_CONTENT)

class CerficateViewSet(viewsets.ModelViewSet):

    queryset = Cerficate.objects.filter(is_active = True)
    serializer_class = CerficateSerializer

    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        instance.is_active = False
        self.perform_update(instance)
        return Response(status=status.HTTP_204_NO_CONTENT)

class ContentViewSet(viewsets.ModelViewSet):

    queryset = Content.objects.filter(is_active = True)
    serializer_class = ContentSerializer

    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        instance.is_active = False
        self.perform_update(instance)
        return Response(status=status.HTTP_204_NO_CONTENT)
