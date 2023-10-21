from django.shortcuts import render
from rest_framework import viewsets
from games.categorie.models import CategoryModel
from games.categorie.serializers import CategorySerializer
from rest_framework.response import Response
from rest_framework import status
from rest_framework.generics import get_object_or_404

# Create your views here.

class CategoryViewSet(viewsets.ModelViewSet):
  queryset = CategoryModel.objects.all()

  ##Traduction en JSON
  serializer_class = CategorySerializer

  def create(self, request, *args, **kwargs):
    serializer = self.get_serializer(data=request.data)
    serializer.is_valid(raise_exception=True)

    self.perform_create(serializer)
    return Response(serializer.data, status=status.HTTP_201_CREATED)
  

  def retrieve(self, request, *args, **kwargs):
    post_id = kwargs.get('pk')
    post = get_object_or_404(CategoryModel, pk=post_id)
    
    serializer = self.get_serializer(post)
    return Response(serializer.data, status=status.HTTP_200_OK)
  
  def partial_update(self, request, *args, **kwargs):
    post_id = kwargs['pk'] ##same as :     post_id = kwargs.get('pk')
    post = get_object_or_404(CategoryModel, pk=post_id)

    serializer = self.get_serializer(post, data=request.data, partial=True)
    serializer.is_valid(raise_exception=True)
    self.perform_update(serializer)
    return Response(serializer.data, status=status.HTTP_200_OK)

  def destroy(self, request, *args, **kwargs):
    post_id = kwargs['pk']
    post = get_object_or_404(CategoryModel, pk=post_id)

    post.delete()
    return Response(status=status.HTTP_204_NO_CONTENT)
  
  