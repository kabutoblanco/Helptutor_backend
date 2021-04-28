from rest_framework import generics, status, viewsets, response
from rest_framework.permissions import IsAuthenticated

from helptutor.users.models import Student
from helptutor.services.models import Offer, Aggrement
from helptutor.services.serializers import *

from drf_yasg.utils import swagger_auto_schema


class OfferAPIView(viewsets.ModelViewSet):

    serializer_class = OfferCreateSerializer
    queryset = Offer.objects.filter(is_active=True)
    permission_classes = (IsAuthenticated, )

    @swagger_auto_schema(
        responses={status.HTTP_200_OK: OfferModelSerializer}
    )
    def create(self, request, *args, **kwargs):
        user = request.user.pk
        student = Student.objects.get(user=user)
        request.data['student'] = student.pk
        return super().create(request, args, kwargs)

    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        instance.is_active = False
        self.perform_update(instance)
        Aggrement.objects.filter(student=instance.student).update(is_active=False)
        return response.Response(status=status.HTTP_204_NO_CONTENT)
