from rest_framework import serializers
from restapp.models import Music

class MusicSerializer(serializers.ModelSerializer):
  class Meta:
    model = Music
    fields = ('id', 'song','singer', 'last_modify_date', 'created')