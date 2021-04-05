from rest_framework import generics, status, viewsets

from helptutor.users.models import Tutor
from helptutor.services.models import Service, Nomination
from helptutor.services.serializers import *

from drf_yasg.utils import swagger_auto_schema


class ServiceAPIView(viewsets.ModelViewSet):

    serializer_class = ServiceCreateSerializer
    queryset = Service.objects.filter(is_active=True)

    @swagger_auto_schema(
        responses={status.HTTP_200_OK: ServiceModelSerializer}
    )
    def create(self, request, *args, **kwargs):
        user = request.user.pk
        tutor = Tutor.objects.get(user=user)
        request.data['tutor'] = tutor.pk
        print(request.data)
        return super().create(request, args, kwargs)

    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        instance.is_active = False
        self.perform_update(instance)
        Nomination.objects.filter(tutor=instance.tutor).update(is_active=False)
        return Response(status=status.HTTP_200_OK)
