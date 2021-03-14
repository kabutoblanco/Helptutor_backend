from rest_framework import generics, viewsets
from users_app.serializers import TutorSerializer
from users_app.models import Tutor

class TutorApi(viewsets.ModelViewSet):

    serializer_class = TutorSerializer
    queryset = Tutor.objects.all()
