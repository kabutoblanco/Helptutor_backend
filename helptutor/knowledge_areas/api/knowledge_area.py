from rest_framework import generics, status, viewsets
from rest_framework.response import Response

from helptutor.knowledge_areas.models import KnowledgeArea
from helptutor.knowledge_areas.serializers import KnowledgeAreaSerializer


class KnowledgeAreaViewSet(viewsets.ModelViewSet):

    queryset = KnowledgeArea.objects.filter(level=0, is_active=True)
    serializer_class = KnowledgeAreaSerializer


class KnowledgeAreaCategoryAPIView(generics.ListAPIView):

    serializer_class = KnowledgeAreaSerializer
    queryset = KnowledgeArea.objects.filter(is_active=True, level=1)

    def list(self, request, *args, **kwargs):
        queryset = KnowledgeArea.objects.filter(knowledge_area=kwargs['pk'], level=1, is_active=True)
        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)