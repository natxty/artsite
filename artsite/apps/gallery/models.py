import os
from django.db import models
from sortable.models import Sortable
from django.conf import settings
from sorl.thumbnail import ImageField
from taggit.managers import TaggableManager
from autoslug import AutoSlugField
from django.db.models import FileField
from django import forms



def work_image_path(instance, filename):
    return os.path.join('images', instance._meta.module_name, instance.slug, filename)

def file_upload_path(instance, filename):
    return os.path.join('downloads', filename)


class Category(models.Model):
    name = models.CharField(max_length=300)
    slug = AutoSlugField(unique=True)
    description =  models.CharField(max_length=300)
    order = models.SmallIntegerField(blank=False, null=False, default=0)

    #if we have a primary Work... show it
    #if not... show a default image
    def get_primary_work(self):
        if self.work_set.filter(is_primary_image=True).count() > 0:
            return self.work_set.filter(is_primary_image=True)[0]
        elif self.work_set.all().count() > 0:
            return self.work_set.all()[0]
        else:
            return None

    @models.permalink
    def get_absolute_url(self):
        return ('artsite.apps.gallery.views.category_landing', [self.slug])

    class Meta:
        verbose_name_plural = 'categories'

    def __unicode__(self):
        return self.name


class Work(models.Model):
    category = models.ForeignKey(Category)
    name = models.CharField(max_length=100)
    slug = AutoSlugField(unique=True)

    #good data:
    date_created = models.DateField()
    medium = models.CharField(max_length=300)
    description = models.TextField(blank=True)
    notes = models.TextField(blank=True)

    image = ImageField(upload_to=work_image_path, blank=False)

    #Work's real-life dimensions:
    height = models.DecimalField(blank=True, null=True, max_digits=5, decimal_places=2)
    width = models.DecimalField(blank=True, null=True, max_digits=5, decimal_places=2)
    depth = models.DecimalField(blank=True, null=True, max_digits=5, decimal_places=2)

    #site stuff:
    order = models.SmallIntegerField(blank=False, null=False, default=0)
    is_primary_image = models.BooleanField()
    
    #these might be nice:
    quote = models.TextField(blank=True)
    quote_byline = models.CharField(max_length=255, blank=True)
    
    #SEO
    meta_title = models.CharField(max_length=100, blank=True)
    meta_keywords = models.TextField(blank=True)
    meta_description = models.TextField(blank=True)

    #tags
    tags = TaggableManager(blank=True)

    @models.permalink
    def get_absolute_url(self):
        return ('artsite.apps.gallery.views.work_landing', [self.category.slug, self.slug])
    
    def __unicode__(self):
        return self.name

    def save(self):
	    if self.is_primary_image:
	        other_primes = Work.objects.filter(category=self.category).filter(is_primary_image = True)
	        for prime in other_primes:
	            prime.is_primary_image = False
	            prime.save()
	    super(Work, self).save()

class Link(models.Model):
    title =  models.CharField(max_length=300)
    url = models.CharField(max_length=300)
    active = models.BooleanField(default=1)
    order = models.SmallIntegerField(blank=True, null=True)

    def __unicode__(self):
        return self.title

class Download(models.Model):
    name = models.CharField(max_length=300)
    download = FileField(upload_to=file_upload_path, blank=False)
    description = models.TextField(blank=True)

    @property
    def file(self):
        return self.download.url
    
    def __unicode__(self):
       return self.name

class ContactForm(forms.Form):
    email = forms.EmailField()
    message = forms.CharField(widget=forms.Textarea)
    #cc_myself = forms.BooleanField(required=False)


