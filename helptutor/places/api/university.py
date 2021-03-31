from rest_framework import generics, status, viewsets
from rest_framework.response import Response

from helptutor.places.serializers import UniversitySerializer
from helptutor.places.models import University


class CityUniversitiesAPIView(generics.ListAPIView):

    serializer_class = UniversitySerializer
    queryset = University.objects.all()

    def list(self, request, *args, **kwargs):
        queryset = University.objects.filter(city=kwargs['pk'])
        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)


class UniversityViewSet(viewsets.ModelViewSet):

    queryset = University.objects.filter(is_active=True)
    serializer_class = UniversitySerializer