from rest_framework import viewsets
from games.gameApi.models import GameModel
from games.gameApi.serializers import GameSerializer
from rest_framework.response import Response
from rest_framework import status
from rest_framework.generics import get_object_or_404
from rest_framework.permissions import IsAuthenticated
from drf_yasg.utils import swagger_auto_schema
from rest_framework import filters
# Create your views here.

class GameViewSet(viewsets.ModelViewSet):
  search_fields = ['title']
  filter_backends = (filters.SearchFilter,)
  queryset = GameModel.objects.all()

  ##Traduction en JSON
  serializer_class = GameSerializer
  permission_classes = [IsAuthenticated]

  @swagger_auto_schema(
    operation_description="Get Game",
  )
  def create(self, request, *args, **kwargs):
    serializer = self.get_serializer(data=request.data)
    serializer.is_valid(raise_exception=True)

    self.perform_create(serializer)
    return Response(serializer.data, status=status.HTTP_201_CREATED)

  @swagger_auto_schema(
    operation_description="Post Game",
  )
  def retrieve(self, request, *args, **kwargs):
    post_id = kwargs.get('pk')
    post = get_object_or_404(GameModel, pk=post_id)
    
    serializer = self.get_serializer(post)
    return Response(serializer.data, status=status.HTTP_200_OK)
  
  @swagger_auto_schema(
    operation_description="Patch Game",
  )
  def partial_update(self, request, *args, **kwargs):
    post_id = kwargs['pk'] ##same as :     post_id = kwargs.get('pk')
    post = get_object_or_404(GameModel, pk=post_id)

    serializer = self.get_serializer(post, data=request.data, partial=True)
    serializer.is_valid(raise_exception=True)
    self.perform_update(serializer)
    return Response(serializer.data, status=status.HTTP_200_OK)

  @swagger_auto_schema(
    operation_description="Delete Game",
  )
  def destroy(self, request, *args, **kwargs):
    post_id = kwargs['pk']
    post = get_object_or_404(GameModel, pk=post_id)

    post.delete()
    return Response(status=status.HTTP_204_NO_CONTENT)
  