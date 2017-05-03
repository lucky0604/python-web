

# Create your views here.
from restapp.models import Music
from restapp.serializers import MusicSerializer

from rest_framework import viewsets

class MusicViewSet(viewsets.ModelViewSet):
  queryset = Music.objects.all()
  serializer_class = MusicSerializer