import os
from django.db import models
from django.conf import settings
from sorl.thumbnail import ImageField
from taggit.managers import TaggableManager


def work_image_path(instance, filename):
    return os.path.join('images', instance._meta.module_name, instance.slug, filename)


class Category(models.Model):
    name = models.CharField(max_length=300)
    slug = models.SlugField()
    description =  models.CharField(max_length=300)

    #Grab the first image as default
    def get_primary_work(self):
        if self.series_set.all().count() > 0:
            return self.series_set.all()[0]
        else:
            return None

    @models.permalink
    def get_absolute_url(self):
        return ('artsite.apps.gallery.views.category_landing', [self.slug])

    class Meta:
        verbose_name_plural = 'categories'

    def __unicode__(self):
        return self.name


class Series(models.Model):
	#Basic Info
    category = models.ForeignKey(Category)
    name = models.CharField('Series Name', max_length=100)
    slug = models.SlugField()
    description = models.TextField()

    order = models.SmallIntegerField(blank=True, null=True)
    date_created = models.DateField()
    
    #SEO Meta
    meta_title = models.CharField(max_length=100, blank=True)
    meta_keywords = models.TextField(blank=True)
    meta_description = models.TextField(blank=True)
    
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
        return ('artsite.apps.gallery.views.series_landing', [self.category.slug, self.slug])

    class Meta:
        verbose_name_plural = 'series'
    
    def __unicode__(self):
        return self.name


class Work(models.Model):
    series = models.ForeignKey(Series)
    name = models.CharField(max_length=100)
    slug = models.SlugField()
    description = models.TextField(blank=True)
    image = ImageField(upload_to=work_image_path, blank=True)
    height = models.SmallIntegerField(blank=True, null=True, height_field=work_height, width_field=work_width)
    width = models.SmallIntegerField(blank=True, null=True)
    depth = models.SmallIntegerField(blank=True, null=True)

    order = models.SmallIntegerField(blank=True, null=True)
    date_created = models.DateTimeField(auto_now_add=True)

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
        cat = self.series.category.slug
        print cat
        return ('artsite.apps.gallery.views.work_landing', [cat, self.series.slug, self.slug])

    class Meta:
        ordering = ['order']
    
    def __unicode__(self):
        return self.name

    def save(self):
	    if self.is_primary_image:
	        other_primes = Work.objects.filter(series=self.series).filter(is_primary_image = True)
	        for prime in other_primes:
	            prime.is_primary_image = False
	            prime.save()
	    super(Work, self).save()

