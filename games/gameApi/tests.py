from django.contrib.auth.models import User
from rest_framework.test import APITestCase
from rest_framework import status
from games.gameApi.models import GameModel
from games.categorie.models import CategoryModel

# Create your tests here.
class GameViewSetTests(APITestCase):

  def setUp(self):
    self.superuser = User.objects.create_superuser(username='adminTest', password='azerty123456', email='admintest@test.com')
    categorie = CategoryModel.objects.create(name='TEST')

    self.client.force_authenticate(user=self.superuser)

    self.game_data = {
      'title': 'title',
      'desc': 'description',
      'addedDate': '2023-10-20',
      'categorie': categorie,
      'plateform': 'game plateforme'
    }

    self.test_game = GameModel.objects.create(**self.game_data)

  #GET GAMES - TEST UNITAIRE
  def test_list_posts(self):
    response = self.client.get('/games/')

    self.assertEqual(response.status_code, status.HTTP_200_OK)

    self.assertGreater(len(response.data), 0)

  def test_create_game(self):
    url = '/games/'
    response = self.client.post(url, self.game_data, format='json')
    self.assertEqual(response.status_code, status.HTTP_201_CREATED)
    self.assertEqual(GameModel.objects.count(), 2)