from rest_framework import generics, viewsets
from rest_framework.response import Response
from rest_framework import status
from .serializers import * 
from .models import (
    KnowledgeArea,
    KnowledgeArea_Tutor,
    KnowledgeArea_Student,
    Certificate,
    Content,
)
from users_app.models import Tutor

from services_app.models import Service, Aggrement, Nomination
 
class KnowledgeAreaViewSet(viewsets.ModelViewSet):

    queryset = KnowledgeArea.objects.filter(is_active = True, level = 0)
    serializer_class = KnowledgeAreaSerializer

    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        instance.is_active = False
        self.perform_update(instance)
        return Response(status = status.HTTP_200_OK)

class KnowledgeAreaCategoryAPIView(generics.ListAPIView):

    serializer_class = KnowledgeAreaSerializer
    queryset = KnowledgeArea.objects.filter(is_active = True, level = 1)

    def list(self, request, *args, **kwargs):
        queryset = KnowledgeArea.objects.filter(knowledge_area = kwargs['pk'], level = 1)
        if queryset.exists():
            serializer = self.get_serializer(queryset, many=True)
            return Response(serializer.data, status = status.HTTP_200_OK)
        return Response({'detail':'No hay subcategorías registradas'},status = status.HTTP_400_BAD_REQUEST)
        

class KnowledgeArea_TutorViewSet(viewsets.ModelViewSet):

    queryset = KnowledgeArea_Tutor.objects.filter(is_active = True)
    serializer_class = KnowledgeArea_TutorSerializer

    def create(self, request, *args, **kwargs):
        request.data['tutor'] = Tutor.objects.get(user=request.data.pop('user')).pk
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        knowledge_area_tutor = serializer.save()
        return Response(
            KnowledgeArea_TutorSerializer(
                knowledge_area_tutor, context=self.get_serializer_context()).data,
        )

    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        instance.is_active = False
        id_tutor = instance.tutor.id
        Service.objects.filter(id = instance.id, tutor = id_tutor).update(is_active = False)
        self.perform_update(instance)
        if KnowledgeArea_Tutor.objects.filter(is_active = True, tutor = id_tutor).exists() == False:
            Nomination.objects.filter(tutor = id_tutor).update(is_active = False)
        return Response(status=status.HTTP_200_OK)

class KnowledgeArea_StudentViewSet(viewsets.ModelViewSet):

    queryset = KnowledgeArea_Student.objects.filter(is_active = True)
    serializer_class = KnowledgeArea_StudentSerializer

    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        instance.is_active = False
        self.perform_update(instance)
        return Response(status=status.HTTP_200_OK)

class CertificateViewSet(viewsets.ModelViewSet):

    queryset = Certificate.objects.filter(is_active = True)
    serializer_class = CertificateSerializer

    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        instance.is_active = False
        id_knowledge_area_tutor = instance.knowledge_area_tutor.id
        self.perform_update(instance)
        if Certificate.objects.filter(is_active = True, knowledge_area_tutor = id_knowledge_area_tutor).exists() == False:
            Service.objects.filter(knowledgeArea_Tutor = id_knowledge_area_tutor).update(is_active = False)
            queryset_list = Service.objects.filter(knowledgeArea_Tutor = id_knowledge_area_tutor)
            for id_k in queryset_list:
                Aggrement.objects.filter(service = id_k.id).update(is_active = False)

        return Response(status=status.HTTP_200_OK)

class ContentViewSet(viewsets.ModelViewSet):

    queryset = Content.objects.filter(is_active = True)
    serializer_class = ContentSerializer

    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        instance.is_active = False
        self.perform_update(instance)
        return Response(status=status.HTTP_200_OK)


#complementarias

class TutorSpecialitiesAPIList(generics.ListAPIView):

    queryset = KnowledgeArea_Tutor.objects.all()
    serializer_class = KnowledgeArea_TutorViewSerializer

    def list(self, request, *args, **kwargs):
        #pk: corresponde al id del tutor
        queryset = KnowledgeArea_Tutor.objects.filter(tutor=kwargs['pk'])
        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data, status = status.HTTP_200_OK)

