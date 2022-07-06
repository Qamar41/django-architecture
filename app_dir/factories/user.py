import factory
from faker import Factory
from django.contrib.auth import get_user_model
from ..user.models import User
import factory.fuzzy
faker = Factory.create()


class UserFactory(factory.DjangoModelFactory):
    class Meta:
        model = User

    firstName = faker.first_name()
    lastName=faker.last_name()
    email = faker.email()
    password = faker.password()
    is_activated = factory.fuzzy.FuzzyChoice(choices=[True, True, True, False])