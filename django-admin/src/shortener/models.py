from django.db import models

from .utils import code_generator, create_shortcode


class SoftURLManager(models.Manager):
    def all(self, *args, **kwargs):
        return super(SoftURLManager, self).all(*args, **kwargs).filter(active = True)

    def refresh_shortcode(self):
        qs = SoftURL.objects.filter(id__gte = 1)
        new_code = 0
        for q in qs:
            q.shortcode = create_shortcode(q)
            q.save()
            new_code += 1
        return 'New Codes made: {i}'.format(i = new_code)


# Create your models here.
class SoftURL(models.Model):
    url = models.CharField(max_length = 220,)
    shortcode = models.CharField(max_length = 15, unique = True, blank = True)
    updated = models.DateTimeField(auto_now = True)    # everytime the model is saved
    timestamp = models.DateTimeField(auto_now_add = True)    # when model was created
    active = models.BooleanField(default = True)

    # built-in objects, it will override query set objects(e.g: Models.objects.all())
    objects = SoftURLManager()
    # if don't wanna override, use another name
    # some_random = SoftURLManager()
    # and then query set will be: Models.objects.some_random()

    # override the save method
    def save(self, *args, **kwargs):
        if self.shortcode is None or self.shortcode == "":
            self.shortcode = create_shortcode(self)
        super(SoftURL, self).save(*args, **kwargs)

    def __str__(self):
        return str(self.url)

		# return str(self.url)

    def __unicode__(self):
        return str(self.url)
