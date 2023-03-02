from django.test import TestCase
from rest_framework import status
from django.urls import reverse
from rest_framework.test import APIClient
from rest_framework.authtoken.models import Token

from users.models import CustomUser

ACTION_URL = reverse('api:transaction-list')
STATISTIC_URL = reverse('api:statistic')


class PublicApiTest(TestCase):
    """Test unauthenticated recipe API request"""

    def setUp(self):
        self.client = APIClient()

    def test_account_auth_required(self):
        res = self.client.get(STATISTIC_URL)
        self.assertEqual(res.status_code, status.HTTP_401_UNAUTHORIZED)


class PrivateApiTest(TestCase):
    """Test authenticated API request"""

    def setUp(self):
        """Create user and Token"""
        user_test = CustomUser.objects.create(username='testuser', password='1q2w3e!')
        user_test.save()
        self.token_user_test = Token.objects.create(user=user_test)
        self.client = APIClient()

    def test_statistic_auth(self):
        self.client.credentials(HTTP_AUTHORIZATION='Token ' + self.token_user_test.key)
        response = self.client.get(STATISTIC_URL)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
