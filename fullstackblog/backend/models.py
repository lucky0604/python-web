from django.db import models

# Create your models here.
from django.contrib.auth.models import User
from django.db import models
import uuid
'''
import token based auth
'''
from django.conf import settings
from django.db.models.signals import post_save
from django.dispatch import receiver
from rest_framework.authtoken.models import Token

@receiver(post_save, sender = settings.AUTH_USER_MODEL)
def create_auth_token(sender, instance = None, created = False, **kwargs):
    if created:
        Token.objects.create(user = instance)

ROLE_CHOICES = (
    ('Admin', 'admin'),
    ('Editor', 'editor'),
    ('Guest', 'guest')
)

class Account(models.Model):
    displayName = models.CharField(blank = False, max_length = 255)
    user = models.OneToOneField(User, on_delete = models.CASCADE)
    username = models.CharField(max_length = 255, blank = True)
    id = models.UUIDField(primary_key = True, default = uuid.uuid4, editable = False)
    role = models.CharField(choices = ROLE_CHOICES, max_length = 20)

    def __str__(self):
        return self.user.username
