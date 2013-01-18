from models import Post
from django.contrib import admin
from django.conf import settings
from django.contrib.admin import site, ModelAdmin

import models

def prepend_static_url(path):
    return settings.STATIC_URL + path

# we define our resources to add to admin pages
class CommonMedia:

    [prepend_static_url(path) for path in (
        'js/admin.js',)]

    js = (
        'https://ajax.googleapis.com/ajax/libs/dojo/1.6.0/dojo/dojo.xd.js',
        prepend_static_url('admin/js/editor.js'),
    )
    css = {
        'all': (prepend_static_url('admin/css/editor.css'),),
    }


admin.site.register(Post,
    Media = CommonMedia,
)