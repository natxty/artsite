import re
import datetime
from django.utils import formats
from django.core import serializers
from django.shortcuts import render
from django.http import Http404, HttpResponse
from models import Response
 




def ajax_obot_response(request):
    """
    Returns what?

    returns: HTML I think
    """
    #some helpful variables:
    now = datetime.datetime.now()
    formatted_now = formats.date_format(now, "TIME_FORMAT")
    formatted_date = formats.date_format(now, "DATE_FORMAT")

    req = request.GET.get('msg', '')

    #regex preps for fun and profit
    greet = re.compile('[Hh](i|ey|ello)')
    name = re.compile('(.*)([Yy]our ){0,1}name') #this is tricky but could be radically improved...
    time = re.compile('(([Ww]hat ){0,1}time is it(\?){0,4})')
    date = re.compile("((.*)(('|i)s ){0,1}the date(\?){0,4})")

    if name.match(req):
        return HttpResponse('My name is John')
    if greet.match(req):
        return HttpResponse('Hi there')
    if time.match(req):
        resp = "It is now %s" % formatted_now
        return HttpResponse(resp)
    if date.match(req):
        resp = "It's %s" % formatted_date
        return HttpResponse(resp)
    else:
        resp = Response.objects.order_by('?')[0]
        return HttpResponse(resp.response)
