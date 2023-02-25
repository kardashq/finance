from django.test import TestCase
from django.contrib.auth import get_user_model

from rest_framework.test import APIClient
from rest_framework import status

CREATE_USER_URL = '/auth/users/'
TOKEN_URL = '/auth/token/login/'


def create_user(**params):
    return get_user_model().objects.create_user(**params)


class PublicUserApiTest(TestCase):
    """Test the user api public"""

    def setUp(self):
        self.client = APIClient()

    def test_create_valid_user_success(self):
        """test creating user with valid payload is successfull"""
        payload = {
            'username': 'testusername',
            'email': 'test@mail.com',
            'password': 'trypassfortest1!',
            're_password': 'trypassfortest1!'
        }
        res = self.client.post(CREATE_USER_URL, payload)

        self.assertEqual(res.status_code, status.HTTP_201_CREATED)
        user = get_user_model().objects.get(email=payload['email'])
        self.assertTrue(user.check_password(payload['password']))
        self.assertNotIn('password', res.data)

    def test_user_exists(self):
        """Test creating user that already exists"""
        payload1 = {
            'username': 'testusername',
            'email': 'test@mail.com',
            'password': 'trypassfortest1!',
        }

        payload2 = {
            'username': 'testusername',
            'email': 'test@mail.com',
            'password': 'trypassfortest1!',
            're_password': 'trypassfortest1!'
        }

        create_user(**payload1)

        res = self.client.post(CREATE_USER_URL, payload2)

        self.assertEqual(res.status_code, status.HTTP_400_BAD_REQUEST)

    def test_password_too_short(self):
        """Test that password must be more than 5 characters"""
        payload = {
            'username': 'testuser',
            'email': 'test@gmail.com',
            'password': 'ha',
            're_password2': 'ha'
        }
        res = self.client.post(CREATE_USER_URL, payload)

        self.assertEqual(res.status_code, status.HTTP_400_BAD_REQUEST)
        user_exists = get_user_model().objects.filter(
            email=payload['email']
        ).exists()
        self.assertFalse(user_exists)

    def test_create_token_for_user(self):
        """Test that a token created for user"""
        payload = {
            'username': 'testusername',
            'email': 'test@mail.com',
            'password': 'trypassfortest1!',
        }
        create_user(**payload)
        res = self.client.post(TOKEN_URL, {'username': payload['username'],
                                           'password': payload['password']})
        self.assertIn('auth_token', res.data)
        self.assertEqual(res.status_code, status.HTTP_200_OK)

    def test_create_token_invalid_credential(self):
        """Test that token is not created when
           invalid credential are given"""
        payload = {
            'email': 'test@mail.com',
            'password': 'trypassfortest1!',
            'username': 'testuser'
        }
        create_user(**payload)

        payload2 = {
            'email': 'test@mail.com',
            'password': 'wrong'
        }
        res = self.client.post(TOKEN_URL, payload2)

        self.assertNotIn('auth_token', res.data)
        self.assertEqual(res.status_code, status.HTTP_400_BAD_REQUEST)

    def test_create_token_no_user(self):
        """Test that token is not created if user doesn't exists"""
        payload = {
            'username': 'test4user',
            'email': 'test4@gmail.com',
            'password': 'testpass'
        }
        res = self.client.post(TOKEN_URL, payload)

        self.assertNotIn('auth_token', res.data)
        self.assertEqual(res.status_code, status.HTTP_400_BAD_REQUEST)

    def test_create_token_missing_field(self):
        """Test that email and password are required"""
        res = self.client.post(TOKEN_URL, {'email': 'test@gmai.com', 'password': ''})

        self.assertNotIn('auth_token', res.data)
        self.assertEqual(res.status_code, status.HTTP_400_BAD_REQUEST)
