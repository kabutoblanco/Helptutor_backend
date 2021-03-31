from rest_framework import status, viewsets
from rest_framework.response import Response

from helptutor.knowledge_areas.serializers import CertificateSerializer
from helptutor.knowledge_areas.models import Certificate
from helptutor.services.models import Service, Aggrement


class CertificateViewSet(viewsets.ModelViewSet):

    queryset = Certificate.objects.filter(is_active=True)
    serializer_class = CertificateSerializer

    def destroy(self, request, pk=None):
        instance = self.get_object()
        instance.is_active = False
        self.perform_update(instance)
        if Certificate.objects.filter(
            is_active=True, 
            knowledge_area_tutor=instance.knowledge_area_tutor.id
        ).exists() == False:
            Service.objects.filter(knowledgeArea_Tutor=id_knowledge_area_tutor).update(is_active=False)
            queryset_list = Service.objects.filter(knowledgeArea_Tutor=id_knowledge_area_tutor)
            for id_k in queryset_list:
                Aggrement.objects.filter(service=id_k.id).update(is_active=False)        
        return Response(status=status.HTTP_200_OK)