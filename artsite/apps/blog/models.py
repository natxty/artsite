from django.db import models

# Create your models here.

class Post(models.Model):
	title = models.CharField(max_length=100)
	author = models.CharField(max_length=100)
	main_content = models.TextField()
	sub_content = models.TextField()
	post_date = models.DateTimeField(auto_now=True)
	
	def __unicode__(self):
		return self.title

	def __str__(self):
		return self.title