from django import template
from django.conf import settings
from artsite.apps.gallery.models import Category, Work

import re

register = template.Library()


@register.simple_tag(takes_context=True)
def get_categories(context):
    ret = []
    categories = Category.objects.all().order_by('order')
    context['categories'] = categories
    return u''


## tags.py
@register.simple_tag
def active(request, pattern):
    if re.search(pattern, request.path):
        return 'active'
    return ''