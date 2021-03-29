from rest_framework import generics, status, viewsets
from rest_framework.response import Response

from helptutor.knowledge_areas.models import KnowledgeArea_Tutor
from helptutor.knowledge_areas.serializers import KnowledgeArea_TutorSerializer, KnowledgeArea_TutorViewSerializer

from helptutor.users.models import Tutor
from helptutor.services.models import Service


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

    def partial_update(self, request, pk=None, **kwargs):
        partial = kwargs.pop('partial', False)
        request.data['tutor'] = Tutor.objects.get(user=request.data.pop('user')).pk
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


class TutorSpecialitiesAPIList(generics.ListAPIView):

    queryset = KnowledgeArea_Tutor.objects.all()
    serializer_class = KnowledgeArea_TutorViewSerializer

    def list(self, request, *args, **kwargs):
        #pk: corresponde al id del tutor
        queryset = KnowledgeArea_Tutor.objects.filter(tutor__user=kwargs['pk'], is_active=True)
        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data, status = status.HTTP_200_OK)