from django.urls import include, path
from django.contrib import admin
from django.urls import path
from rest_framework import routers
from games.gameApi.views import GameViewSet
from games.categorie.views import CategoryViewSet

router = routers.DefaultRouter()
router.register(r'games', GameViewSet)
router.register(r'categorie', CategoryViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
