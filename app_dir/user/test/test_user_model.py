
from django.test import TestCase
from django.contrib.auth import get_user_model

User = get_user_model()


class StudentTest(TestCase):
    def setUp(self):
        self.data = {

            'email': 'peter@example.com',
            'password':'12345'
        }
        self.instance = User(**self.data)

    def test_model_can_create_instance(self):
        """ Test if the model can create an instance."""
        old_count = User.objects.count()
        self.instance.save()
        new_count = User.objects.count()

        self.assertNotEqual(old_count, new_count)
        self.assertEqual(self.instance.email, self.data.get('email'))
