from django.core.urlresolvers import reverse
from rest_framework.test import APITestCase
from django.contrib.auth.models import User
from rest_framework import status

# Create your tests here.

class AccountsTest(APITestCase):
    def setUp(self):
        self.test_user = User.objects.create_user('testuser', 'test@example.com', 'testpassword')

        # url for creating an account
        self.create_url = reverse('account-create')

    def test_create_user(self):
        # ensure create a new user and a valid token is crated with it
        data = {
            'username': 'foobar',
            'email': 'foobar@example.com',
            'password': 'somepassword'
        }
        response = self.client.post(self.create_url, data, format = 'json')

        # make sure there are two users in the database
        self.assertEqual(User.objects.count(), 2)
        # returning a 201 created code
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)


    '''
    check the password field
    '''
    def test_create_user_with_short_password(self):
        data = {
            'username': 'foobar',
            'email': 'foobar@example.com',
            'password': 'foo'
        }
        response = self.client.post(self.create_url, data, format = 'json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertEqual(User.objects.count(), 1)
        self.assertEqual(len(response.data['password']), 1)

    def test_create_user_with_no_password(self):
        data = {
            'username': 'foobar',
            'email': 'foobarbaz@example.com',
            'password': ''
        }
        response = self.client.post(self.create_url, data, format = 'json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertEqual(User.objects.count(), 1)
        self.assertEqual(len(response.data['password']), 1)


    '''
    check the username field
    '''
    def test_create_user_with_too_long_username(self):
        data = {
            'username': 'foo'*30,
            'email': 'foobar@example.com',
            'password': 'foobar'
        }
        response = self.client.post(self.create_url, data, format = 'json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertEqual(User.objects.count(), 1)
        self.assertEqual(len(response.data['username']), 1)

    def test_create_user_with_no_username(self):
        data = {
            'username': '',
            'email': 'foobar@example.com',
            'password': 'foobar'
        }
        response = self.client.post(self.create_url, data, format = 'json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertEqual(User.objects.count(), 1)
        self.assertEqual(len(response.data['username']), 1)

    def test_create_user_with_preexisting_username(self):
        data = {
            'username': 'testuser',
            'email': 'foobarbaz@example.com',
            'password': 'testuser'
        }
        response = self.client.post(self.create_url, data, format = 'json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertEqual(User.objects.count(), 1)
        self.assertEqual(len(response.data['username']), 1)


    '''
    check the email field
    '''
    def test_create_user_with_preexisting_email(self):
        data = {
            'username': 'testuser2',
            'email': 'test@example.com',
            'password': 'testuser'
        }
        response = self.client.post(self.create_url, data, format = 'json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertEqual(User.objects.count(), 1)
        self.assertEqual(len(response.data['email']), 1)

    def test_create_user_with_invalid_email(self):
        data = {
            'username': 'foobarbaz',
            'email': 'testing',
            'password': 'testuser'
        }
        response = self.client.post(self.create_url, data, format = 'json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertEqual(User.objects.count(), 1)
        self.assertEqual(len(response.data['email']), 1)

    def test_create_user_with_no_email(self):
        data = {
            'username': 'foobar',
            'email': '',
            'password': 'testuser'
        }
        response = self.client.post(self.create_url, data, format = 'json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertEqual(User.objects.count(), 1)
        self.assertEqual(len(response.data['email']), 1)
