from django.db import models
import datetime
import jwt

ROLES = (
    ('customer', 'Customer'),
)
GENDER=(
('male','Male'),
('female','Female'),
('other','Other')
)

# Create your models here.
class User(models.Model):
    firstName = models.CharField(max_length=100, blank=True, null=True)
    lastName = models.CharField(max_length=100, blank=True, null=True)
    email = models.CharField(max_length=100)
    password = models.CharField(max_length=1000)
    phoneNumber = models.CharField(max_length=20, blank=True,null=True)
    gender = models.CharField(max_length=100, blank=False, default=GENDER[0][0], choices=GENDER)
    role = models.CharField(max_length=100, blank=False, default=ROLES[0][0], choices=ROLES)
    birth_date = models.DateTimeField(blank=True,null=True)
    is_activated = models.BooleanField()
    created_at = models.DateTimeField(auto_now_add=True)

    def encode_auth_token(self, user_id):
        """
            Generates the Auth Token
            :return: string
        """
        try:
            payload = {
                'exp': datetime.datetime.utcnow() + datetime.timedelta(days=1000, seconds=0),
                'iat': datetime.datetime.utcnow(),
                'sub': user_id
            }
            self.token = jwt.encode(
                payload,
                os.getenv('SECRET_KEY'),
                algorithm='HS256')

            return self.token

        except Exception as e:
            return e

    def is_admin(self):
        return self.permission == ACCESS['admin']
