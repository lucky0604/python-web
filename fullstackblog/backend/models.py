from django.conf import settings
from django.db import models
from django.contrib.contenttypes.fields import GenericForeignKey
from django.contrib.contenttypes.models import ContentType
from django.utils import timezone
from django.core.urlresolvers import reverse
from django.contrib.auth.models import User

from rest_framework.authtoken.models import Token as DefaultTokenModel

from .utils import import_callable

TokenModel = import_callable(
    getattr(settings, 'REST_AUTH_TOKEN_MODEL', DefaultTokenModel)
)

class PublishedManager(models.Manager):
    def get_queryset(self):
        return super(PublishedManager, self).get_queryset().filter(status = 'published')

class Articles(models.Model):
    STATUS_CHOICES = (
        ('Draft', 'draft'),
        ('Published', 'published'),
    )
    title = models.CharField(max_length = 255)
    author = models.ForeignKey(User, related_name = 'blog_articles')
    
    content = models.TextField()
    slug = models.SlugField(max_length = 255, unique_for_date = 'publish')
    created_time = models.DateTimeField(auto_now_add = True)
    updated_time = models.DateTimeField(auto_now = True)
    publish = models.DateTimeField(default = timezone.now)
    status = models.CharField(max_length = 10, choices = STATUS_CHOICES, default = 'Published')


    objects = models.Manager()
    published = PublishedManager

    class Meta:
        ordering = ('-publish',)

    def __str__(self):
        return self.title
    
    def get_absolute_url(self):
        return reverse('article:detail', args = [self.publish.year, self.publish.strftime('%m'), self.publish.strftime('%d'), self.slug])
