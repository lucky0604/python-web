from django.conf import settings
from django.db import models
from django.db.models.signals import pre_save
from django.contrib.contenttypes.fields import GenericForeignKey
from django.contrib.contenttypes.models import ContentType
from django.utils import timezone
from django.core.urlresolvers import reverse
from django.contrib.auth.models import User
from django.utils.text import slugify
from django.utils.safestring import mark_safe

from markdown_deux import markdown

from rest_framework.authtoken.models import Token as DefaultTokenModel

from .utils import import_callable, get_read_time

TokenModel = import_callable(
    getattr(settings, 'REST_AUTH_TOKEN_MODEL', DefaultTokenModel)
)

class PostManager(models.Manager):
    def active(self, *args, **kwargs):
        return super(PostManager, self).filter(draft = False).filter(publish__lte = timezone.now())

def upload_location(instance, filename):
    PostModel = instance.__class__
    new_id = PostModel.objects.order_by('id').last().id + 1

    return "%s/%s" %(new_id, filename)

class Post(models.Model):
    user = models.ForeignKey(User, default = 1)
    title = models.CharField(max_length = 120)
    slug = models.SlugField(unique = True)
    content = models.TextField()
    draft = models.BooleanField(default = False)
    publish = models.DateField(auto_now = False, auto_now_add = False)
    read_time = models.IntegerField(default = 0)
    updated = models.DateTimeField(auto_now = True, auto_now_add = False)
    timestamp = models.DateTimeField(auto_now = False, auto_now_add = True)

    objects = PostManager()


    def __str__(self):
        return self.title


    def get_absolute_url(self):
        return reverse('posts:detail', kwargs = {'slug': self.slug})

    def get_api_url(self):
        return reverse('posts-api:detail', kwargs = {'slug': self.slug})


    class Meta:
        ordering = ['-timestamp', '-updated']

    def get_markdown(self):
        content = self.content
        markdown_text = markdown(content)
        return mark_safe(markdown_text)

def create_slug(instance, new_slug = None):
    slug = slugify(instance.title)
    if new_slug is not None:
        slug = new_slug
    qs = Post.objects.filter(slug = slug).order_by('-id')
    exists = qs.exists()
    if exists:
        new_slug = '%s-%s' %(slug, qs.first().id)
        return create_slug(instance, new_slug = new_slug)
    return slug

def pre_save_post_receiver(sender, instance, *args, **kwargs):
    if not instance.slug:
        instance.slug = create_slug(instance)

    if instance.content:
        html_string = instance.get_markdown()
        read_time_var = get_read_time(html_string)
        instance.read_time = read_time_var


pre_save.connect(pre_save_post_receiver, sender = Post)
