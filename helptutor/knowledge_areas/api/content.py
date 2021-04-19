from rest_framework import status, viewsets
from rest_framework.response import Response

from helptutor.knowledge_areas.models import Content
from helptutor.knowledge_areas.serializers import ContentSerializer


class ContentViewSet(viewsets.ModelViewSet):

    queryset = Content.objects.filter(is_active=True)
    serializer_class = ContentSerializer

    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        instance.is_active = False
        self.perform_update(instance)
        return Response(status=status.HTTP_204_NO_CONTENT)
