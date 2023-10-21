from rest_framework import serializers
from games.gameApi.models import GameModel

class GameSerializer(serializers.HyperlinkedModelSerializer):
  class Meta: 
    model = GameModel
    fields = '__all__'

