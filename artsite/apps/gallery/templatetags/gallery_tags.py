from django import template
from django.conf import settings
from artsite.apps.gallery.models import Category, Series, Work

register = template.Library()

@register.tag
def get_series_by_category(parser, token):
    """
    Returns a list of dictionaries for categories, with the contained series
    objects under each category.
    
    [{'category':'Large Works', 'series':[<Series object>, <eries Object>, .. ] } ]
    
    Usage:
    {% get_series_by_category as cat %}
    """
    bits = token.contents.split()
    if bits[1] != 'as' or len(bits) < 3:
        raise template.TemplateSyntaxError, "%r usage: {% %r as variable_name %}" % (bits[0], bits[0])
    return SeriesByCategory(bits[2])

class SeriesByCategory(template.Node):
    def __init__(self, variable_name):
        self.variable_name = variable_name

    def render(self, context):
        ret = []
        for c in Category.objects.all():
            ret.append({'category': c, 'series': c.series_set.all().order_by('order')})
        context[self.variable_name] = ret
        return ''

@register.simple_tag(takes_context=True)
def get_categories(context):
    ret = []
    categories = Category.objects.all()
    context['categories'] = categories
    return u''