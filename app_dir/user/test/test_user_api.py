from django.test import TestCase
from django.urls import reverse
from rest_framework.test import APIClient
from faker import Factory
from app_dir.factories import UserFactory

faker = Factory.create()


class UserTest(TestCase):
    def setUp(self):
        self.user = UserFactory()
        self.client = APIClient()
        # self.client.force_authenticate(user=self.user)

        self.namespace = 'user_api'
        self.body = {
            'firstName': faker.first_name(),
            'email': faker.email(),
            'password': faker.password()

        }
        self.create_url = reverse(self.namespace + ':user-creator')
        self.list_url = reverse(self.namespace + ':user-list')

    def test_create_user_api(self):
        response = self.client.post(self.create_url, self.body, format='json')
        self.assertEqual(401, response.status_code)

