from rest_framework import viewsets
from games.gameApi.models import GameModel
from games.gameApi.serializers import GameSerializer
from rest_framework.response import Response
from rest_framework import status
# Create your views here.

class GameViewSet(viewsets.ModelViewSet):
  queryset = GameModel.objects.all()

  ##Traduction en JSON
  serializer_class = GameSerializer

  def create(self, request, *args, **kwargs):
    serializer = self.get_serializer(data=request.data)
    serializer.is_valid(raise_exception=True)

    self.perform_create(serializer)
    return Response(serializer.data, status=status.HTTP_201_CREATED)
  