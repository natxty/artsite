from django import template
from django.conf import settings

from datetime import datetime

register = template.Library()


@register.simple_tag(takes_context=True)
def in_studio(context):
    now = datetime.now()
    hour = now.strftime('%H')

    # arbitrary hours, between 8am and 8pm
    # Time-Zone?
    if (hour >= 8 <= 20):
    	return 'in studio'
    else:
    	return 'out of studio'

