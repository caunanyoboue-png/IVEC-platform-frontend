from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from .models import User

class UserTests(APITestCase):
    def setUp(self):
        self.user_data = {
            'username': 'testuser',
            'password': 'testpassword',
            'role': 'Investisseur'
        }
        self.user = User.objects.create_user(**self.user_data)

    def test_user_creation(self):
        response = self.client.post(reverse('user-list'), self.user_data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(User.objects.count(), 2)  # 1 from setUp + 1 new user
        self.assertEqual(User.objects.get(username='testuser').role, 'Investisseur')

    def test_user_login(self):
        response = self.client.post(reverse('user-login'), {
            'username': 'testuser',
            'password': 'testpassword'
        })
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertIn('token', response.data)

    def test_user_list(self):
        response = self.client.get(reverse('user-list'))
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)  # Only the user created in setUp

    def test_user_detail(self):
        response = self.client.get(reverse('user-detail', args=[self.user.id]))
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['username'], self.user.username)

    def test_user_update(self):
        response = self.client.patch(reverse('user-detail', args=[self.user.id]), {
            'role': 'Admin'
        })
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.user.refresh_from_db()
        self.assertEqual(self.user.role, 'Admin')

    def test_user_delete(self):
        response = self.client.delete(reverse('user-detail', args=[self.user.id]))
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(User.objects.count(), 0)  # User should be deleted