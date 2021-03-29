from rest_framework import generics, status, viewsets
from rest_framework.response import Response

from helptutor.places.serializers import StateSerializer
from helptutor.places.models import State


class CountryStatesAPIView(generics.ListAPIView):

    serializer_class = StateSerializer
    queryset = State.objects.all()

    def list(self, request, *args, **kwargs):
        queryset = State.objects.filter(country=kwargs['pk'])
        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)


class StateViewSet(viewsets.ModelViewSet):

    queryset = State.objects.filter(is_active=True)
    serializer_class = StateSerializer