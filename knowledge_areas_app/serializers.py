from rest_framework import serializers

from .models import (
    KnowledgeArea,
    KnowledgeArea_Tutor,
    KnowledgeArea_Student,
    Cerficate,
    Content,
)
 

class KnowledgeAreaSerializer(serializers.ModelSerializer):

    class Meta:
        model = KnowledgeArea
        fields = '__all__'

class KnowledgeArea_TutorSerializer(serializers.ModelSerializer):

    class Meta:
        model = KnowledgeArea_Tutor
        fields = '__all__'

class KnowledgeArea_StudentSerializer(serializers.ModelSerializer):

    class Meta:
        model = KnowledgeArea_Student
        fields = '__all__'  

class CerficateSerializer(serializers.ModelSerializer):

    class Meta:
        model = Cerficate
        fields = '__all__'  

class ContentSerializer(serializers.ModelSerializer):

    class Meta:
        model = Content
        fields = '__all__'  
