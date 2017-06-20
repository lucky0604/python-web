from django.db import models

# Create your models here.
from django.contrib.auth.models import User
from django.db import models
import uuid

class Account(models.Model):
    displayName = models.CharField(blank = False, max_length = 255)
    user = models.OneToOneField(User, on_delete = models.CASCADE)
    username = models.CharField(max_length = 255, blank = True)
    id = models.UUIDField(primary_key = True, default = uuid.uuid4, editable = False)

    def __str__(self):
        return self.user.username
