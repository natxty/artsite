from django.db import models

class Response(models.Model):
    slug = models.SlugField(max_length=255, unique=True, help_text='A shortname/identifier for the response.')
    response = models.TextField()

    class Meta:
        verbose_name_plural = 'Obot Responses'

    def __unicode__(self):
        return self.slug

    def save(self):
        super(Response, self).save()


class Log(models.Model):

    timestamp = models.DateTimeField(auto_now=True)
    author = models.CharField(max_length=255)
    content = models.CharField(max_length=255)

    def save(self):
        super(Log, self).save()


