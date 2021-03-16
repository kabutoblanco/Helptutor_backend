from rest_framework import generics, viewsets
from .serializers import CountrySerializer, StateSerializer, CitySerializer, UniversitySerializer
from .models import Country, State, City, University
from rest_framework.response import Response
from rest_framework import status


class CountryViewSet(viewsets.ModelViewSet):

    queryset = Country.objects.filter(is_active = True)
    serializer_class = CountrySerializer

    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        instance.is_active = False
        self.perform_update(instance)
        return Response(status=status.HTTP_204_NO_CONTENT)


class StateViewSet(viewsets.ModelViewSet):

    queryset = State.objects.filter(is_active = True)
    serializer_class = StateSerializer

    def retrieve(self, request, pk=None):
        queryset = State.objects.filter(country = pk)
        serializer = StateSerializer(queryset, many=True)
        return Response(serializer.data)

    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        instance.is_active = False
        self.perform_update(instance)
        return Response(status=status.HTTP_204_NO_CONTENT)


class CityViewSet(viewsets.ModelViewSet):

    queryset = City.objects.filter(is_active = True)
    serializer_class = CitySerializer

    def retrieve(self, request, pk=None):
        queryset = City.objects.filter(state = pk)
        serializer = CitySerializer(queryset, many=True)
        return Response(serializer.data)

    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        instance.is_active = False
        self.perform_update(instance)
        return Response(status=status.HTTP_204_NO_CONTENT)


class UniversityViewSet(viewsets.ModelViewSet):

    queryset = University.objects.filter(is_active = True)
    serializer_class = UniversitySerializer

    def retrieve(self, request, pk=None):
        queryset = University.objects.filter(city = pk)
        serializer = UniversitySerializer(queryset, many=True)
        return Response(serializer.data)

    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        instance.is_active = False
        self.perform_update(instance)
        return Response(status=status.HTTP_204_NO_CONTENT)
