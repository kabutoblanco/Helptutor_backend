from rest_framework import generics, status, viewsets
from rest_framework.response import Response

from users_app.models import Tutor
from services_app.models import Service, Aggrement, Nomination

from .models import *
from .serializers import * 

 
class KnowledgeAreaViewSet(viewsets.ModelViewSet):

    queryset = KnowledgeArea.objects.filter(level=0, is_active=True)
    serializer_class = KnowledgeAreaSerializer


class KnowledgeAreaCategoryAPIView(generics.ListAPIView):

    serializer_class = KnowledgeAreaSerializer
    queryset = KnowledgeArea.objects.filter(is_active=True, level=1)

    def list(self, request, *args, **kwargs):
        queryset = KnowledgeArea.objects.filter(knowledge_area=kwargs['pk'], level=1, is_active=True)
        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
        

class KnowledgeArea_TutorViewSet(viewsets.ModelViewSet):

    queryset = KnowledgeArea_Tutor.objects.filter(is_active=True)
    serializer_class = KnowledgeArea_TutorSerializer

    def create(self, request, *args, **kwargs):
        request.data['tutor'] = Tutor.objects.get(user=request.data.pop('user')).pk
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        instance = serializer.save()
        return Response(
            KnowledgeArea_TutorViewSerializer(
                instance, context=self.get_serializer_context()).data,
            status=status.HTTP_201_CREATED
        )

    def partial_update(self, request, pk=None):
        partial = kwargs.pop('partial', False)
        instance = KnowledgeArea_Tutor.objects.get(pk=pk)
        serializer = self.get_serializer(data=request.data, instance=instance, partial=partial)
        serializer.is_valid(raise_exception=True)
        isntance = serializer.save()
        return Response(
            KnowledgeArea_TutorViewSerializer(
                instance, context=self.get_serializer_context()).data,
            status=status.HTTP_200_OK
        )

    def destroy(self, request, pk=None):
        instance = KnowledgeArea_Tutor.objects.get(pk=pk)
        instance.is_active = False
        id_tutor = instance.tutor.id
        Service.objects.filter(id=instance.id, tutor=id_tutor).update(is_active=False)
        self.perform_update(instance)
        if KnowledgeArea_Tutor.objects.filter(tutor=id_tutor, is_active=True).exists() == False:
            Nomination.objects.filter(tutor=id_tutor).update(is_active=False)
        return Response(status=status.HTTP_200_OK)


class KnowledgeArea_StudentViewSet(viewsets.ModelViewSet):

    queryset = KnowledgeArea_Student.objects.filter(is_active=True)
    serializer_class = KnowledgeArea_StudentSerializer

    def destroy(self, request, pk=None):
        instance = KnowledgeArea_Student.objects.get(pk=pk)
        instance.is_active = False
        self.perform_update(instance)
        return Response(status=status.HTTP_200_OK)


class CertificateViewSet(viewsets.ModelViewSet):

    queryset = Certificate.objects.filter(is_active=True)
    serializer_class = CertificateSerializer

    def destroy(self, request, pk=None):
        instance = Certificate.objects.get(pk=pk)
        instance.is_active = False
        id_knowledge_area_tutor = instance.knowledge_area_tutor.id
        self.perform_update(instance)
        if Certificate.objects.filter(is_active=True, knowledge_area_tutor=id_knowledge_area_tutor).exists() == False:
            Service.objects.filter(knowledgeArea_Tutor=id_knowledge_area_tutor).update(is_active=False)
            queryset_list = Service.objects.filter(knowledgeArea_Tutor=id_knowledge_area_tutor)
            for id_k in queryset_list:
                Aggrement.objects.filter(service=id_k.id).update(is_active=False)

        return Response(status=status.HTTP_200_OK)


class ContentViewSet(viewsets.ModelViewSet):

    queryset = Content.objects.filter(is_active=True)
    serializer_class = ContentSerializer

    def destroy(self, request, *args, **kwargs):
        instance = Content.objects.get(pk=pk)
        instance.is_active = False
        self.perform_update(instance)
        return Response(status=status.HTTP_200_OK)


#complementarias

class TutorSpecialitiesAPIList(generics.ListAPIView):

    queryset = KnowledgeArea_Tutor.objects.all()
    serializer_class = KnowledgeArea_TutorViewSerializer

    def list(self, request, *args, **kwargs):
        #pk: corresponde al id del tutor
        queryset = KnowledgeArea_Tutor.objects.filter(tutor=kwargs['pk'], is_active=True)
        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data, status = status.HTTP_200_OK)

