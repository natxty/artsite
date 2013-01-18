from django import template
from django.conf import settings
from artsite.apps.gallery.models import Category, Work

register = template.Library()


@register.simple_tag(takes_context=True)
def get_categories(context):
    ret = []
    categories = Category.objects.all()
    context['categories'] = categories
    return u''