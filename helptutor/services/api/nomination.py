from rest_framework import generics, status, viewsets, response
from rest_framework.permissions import IsAuthenticated

from helptutor.users.models import Tutor
from helptutor.services.serializers import *

from drf_yasg.utils import swagger_auto_schema


class NominationAPIView(viewsets.ModelViewSet):

    serializer_class = NominationCreateSerializer
    queryset = Nomination.objects.filter(is_active=True)
    permission_classes = (IsAuthenticated, )

    @swagger_auto_schema(
        responses={status.HTTP_200_OK: NominationModelSerializer}
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
        return response.Response(status=status.HTTP_200_OK)