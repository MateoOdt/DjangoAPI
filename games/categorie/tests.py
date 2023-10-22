from django.contrib.auth.models import User
from rest_framework.test import APITestCase
from rest_framework import status
from .models import CategoryModel

class CategoryModelTests(APITestCase):

    def setUp(self):
        self.superuser = User.objects.create_superuser(username='adminTest', password='azerty123456', email='admintest@test.com')
        self.client.force_authenticate(user=self.superuser)

        self.category_data = {
            'name': 'Test Category Name'
        }

        self.test_category = CategoryModel.objects.create(**self.category_data)

    # GET CATEGORIES - TEST UNITAIRE
    def test_list_categories(self):
        response = self.client.get('/categorie/')

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertGreater(len(response.data), 0)

    # POST CATEGORY - TEST UNITAIRE
    def test_create_category(self):
        response = self.client.post('/categorie/', self.category_data, format='json')

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(CategoryModel.objects.count(), 2)

        self.assertEqual(response.data['name'], 'Test Category Name')

    # PATCH CATEGORY - TEST UNITAIRE
    def test_update_category(self):
        updated_data = {'name': 'Updated Category Name'}
        response = self.client.patch(f'/categorie/{self.test_category.id}/', updated_data, format='json')

        self.assertEqual(response.status_code, status.HTTP_200_OK)

        self.test_category.refresh_from_db()
        self.assertEqual(self.test_category.name, 'Updated Category Name')

    # DELETE CATEGORY - TEST UNITAIRE
    def test_destroy_category(self):
        response = self.client.delete(f'/categorie/{self.test_category.id}/')

        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)

        with self.assertRaises(CategoryModel.DoesNotExist):
            CategoryModel.objects.get(id=self.test_category.id)

    def test_destroy_nonexistent_category(self):
        response = self.client.delete('/categorie/9999/')

        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)