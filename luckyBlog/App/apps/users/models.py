from django.db import models
from django.contrib.auth.models import AbstractUser
from utils.default_model import random_nick_name
from blog.models import Article

# Create your models here.
__all__ = [
    'UserProfile',
    'EmailVerifyCode',
    'Message',
    'Comment',
    'Reply'
]

class UserProfile(AbstractUser):
    gender_choices = (
        ('male', 'Male'),
        ('female', 'Female'),
        ('unknown', 'Unknown')
    )
    nick_name = models.CharField(max_length = 100, default = random_nick_name)
    gender = models.CharField(choices = gender_choices, default = 'unknown', max_length = 20)
    image = models.ImageField(upload_to = 'avatar/%Y/%m', max_length = 100, default = '')

    def get_message_count(self):
        return Message.objects.filter(status = False).count()

    def get_comment_count(self):
        return Comment.objects.filter(status = False).count()

class EmailVerifyCode(models.Model):
    code = models.CharField(max_length = 20, unique = True)
    email = models.EmailField(max_length = 50)
    send_time = models.DateTimeField(auto_now_add = True)

class Message(models.Model):
    add_time = models.DateTimeField(auto_now_add = True)
    body = models.CharField(max_length = 200)
    status = models.BooleanField(default = False)

class Comment(models.Model):
    user = models.ForeignKey(UserProfile)
    article = models.ForeignKey(Article, related_name = 'article_comment')
    body = models.TextField()
    add_time = models.DateTimeField(auto_now_add = True)
    status = models.BooleanField(default = True)

    def get_reply(self):
        return Reply.objects.filter(comment = self.pk)

class Reply(models.Model):
    user = models.ForeignKey(UserProfile)
    comment = models.ForeignKey(Comment)
    body = models.TextField()
    add_time = models.DateTimeField(auto_now_add = True)
