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
        return Response(status=status.HTTP_200_OK)


class CountryStatesAPIView(generics.ListAPIView):

    serializer_class = StateSerializer
    queryset = State.objects.all()

    def list(self, request, *args, **kwargs):
        queryset = State.objects.filter(country = kwargs['pk'])
        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)


class StateViewSet(viewsets.ModelViewSet):

    queryset = State.objects.filter(is_active = True)
    serializer_class = StateSerializer

    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        instance.is_active = False
        self.perform_update(instance)
        return Response(status=status.HTTP_200_OK)

    
class StateCitiesAPIView(generics.ListAPIView):

    serializer_class = CitySerializer
    queryset = State.objects.all()

    def list(self, request, *args, **kwargs):
        queryset = City.objects.filter(state = kwargs['pk'])
        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)


class CityViewSet(viewsets.ModelViewSet):

    queryset = City.objects.filter(is_active = True)
    serializer_class = CitySerializer

    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        instance.is_active = False
        self.perform_update(instance)
        return Response(status=status.HTTP_200_OK)

    
class CityUniversitiesAPIView(generics.ListAPIView):

    serializer_class = UniversitySerializer
    queryset = University.objects.all()

    def list(self, request, *args, **kwargs):
        queryset = University.objects.filter(city = kwargs['pk'])
        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)


class UniversityViewSet(viewsets.ModelViewSet):

    queryset = University.objects.filter(is_active = True)
    serializer_class = UniversitySerializer

    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        instance.is_active = False
        self.perform_update(instance)
        return Response(status=status.HTTP_200_OK)
