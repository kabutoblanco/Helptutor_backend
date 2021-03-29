from rest_framework import serializers

from helptutor.knowledge_areas.models import KnowledgeArea_Student


class KnowledgeArea_StudentSerializer(serializers.ModelSerializer):

    class Meta:
        model = KnowledgeArea_Student
        fields = '__all__'