from .models import Person
from rest_framework import viewsets, permissions
from .serializers import PersonSerializer

class PersonViewSet(viewsets.ModelViewSet):
    queryset=Person.objects.all().order_by('id')
    serializer_class=PersonSerializer
    permission_classes=[permissions.AllowAny]