from rest_framework import generics, viewsets
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

    queryset = KnowledgeArea.objects.all()
    serializer_class = KnowledgeAreaSerializer

class KnowledgeArea_TutorViewSet(viewsets.ModelViewSet):

    queryset = KnowledgeArea_Tutor.objects.all()
    serializer_class = KnowledgeArea_TutorSerializer

class KnowledgeArea_StudentViewSet(viewsets.ModelViewSet):

    queryset = KnowledgeArea_Student.objects.all()
    serializer_class = KnowledgeArea_StudentSerializer

class CerficateViewSet(viewsets.ModelViewSet):

    queryset = Cerficate.objects.all()
    serializer_class = CerficateSerializer

class ContentViewSet(viewsets.ModelViewSet):

    queryset = Content.objects.all()
    serializer_class = ContentSerializer
