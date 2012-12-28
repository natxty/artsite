from django.db import models

class Resume(models.Model):
    name = models.CharField(max_length=300)
    slug = models.SlugField()

    general_description =  models.CharField(max_length=300)

    #Components, we'll add markdown for easier editing:
    solo_exhibitions = models.TextField(blank=True)
    group_exhibitions = models.TextField(blank=True)
    awards_residencies = models.TextField(blank=True)
    bibliography = models.TextField(blank=True)
    current_employment = models.TextField(blank=True)
    public_collection = models.TextField(blank=True)
    education = models.TextField(blank=True)


    class Meta:
    	verbose_name = 'Resume'
        verbose_name_plural = 'Resumes'

    def __unicode__(self):
        return self.name


