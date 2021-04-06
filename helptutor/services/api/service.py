from rest_framework import generics, status, viewsets, mixins, response
from rest_framework.permissions import IsAuthenticated

from helptutor.users.models import Tutor
from helptutor.services.models import Service, Aggrement
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
        return super().create(request, args, kwargs)

    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        instance.is_active = False
        self.perform_update(instance)
        Aggrement.objects.filter(service=instance.pk).update(is_active=False)
        return Response(status=status.HTTP_200_OK)


class TutorServicesAPI(generics.ListAPIView):

    serializer_class = ServiceModelSerializer
    permission_classes = (IsAuthenticated, )

    def get_queryset(self):
        queryset = Service.objects.filter(tutor__user=self.request.user.pk)
        return queryset
