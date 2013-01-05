from models import Post
from django.contrib import admin
from django.contrib.admin import site, ModelAdmin

import models

# we define our resources to add to admin pages
class CommonMedia:
  js = (
    'https://ajax.googleapis.com/ajax/libs/dojo/1.6.0/dojo/dojo.xd.js',
    '/static/admin/js/editor.js',
  )
  css = {
    'all': ('/static/admin/css/editor.css',),
  }


admin.site.register(Post,
	Media = CommonMedia,
)