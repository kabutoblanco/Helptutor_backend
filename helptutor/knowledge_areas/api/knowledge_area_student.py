from rest_framework import status, viewsets
from rest_framework.response import Response
 
from helptutor.knowledge_areas.models import KnowledgeArea_Student
from helptutor.knowledge_areas.serializers import KnowledgeArea_StudentSerializer


class KnowledgeArea_StudentViewSet(viewsets.ModelViewSet):

    queryset = KnowledgeArea_Student.objects.filter(is_active=True)
    serializer_class = KnowledgeArea_StudentSerializer

    def destroy(self, request, pk=None):
        instance = KnowledgeArea_Student.objects.get(pk=pk)
        instance.is_active = False
        self.perform_update(instance)
        return Response(status=status.HTTP_204_NO_CONTENT)
