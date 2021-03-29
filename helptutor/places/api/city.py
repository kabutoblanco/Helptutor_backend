from rest_framework import generics, status, viewsets
from rest_framework.response import Response

from helptutor.places.serializers import CitySerializer
from helptutor.places.models import City, State

    
class StateCitiesAPIView(generics.ListAPIView):

    serializer_class = CitySerializer
    queryset = State.objects.all()

    def list(self, request, *args, **kwargs):
        queryset = City.objects.filter(state=kwargs['pk'])
        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)


class CityViewSet(viewsets.ModelViewSet):

    queryset = City.objects.filter(is_active=True)
    serializer_class = CitySerializer