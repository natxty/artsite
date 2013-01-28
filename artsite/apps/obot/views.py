import re, os, datetime, aiml
from django.conf import settings
from django.utils import formats
from django.core import serializers
from django.shortcuts import render
from django.http import Http404, HttpResponse
from models import Response
 




def ajax_obot_response(request):
    """
    Simple regex-based response kit
    returns: HTML
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

def _local_ajax_obot_response(req):
    """
    Simple regex-based response kit
    returns: HTML
    """

    #some helpful variables:
    now = datetime.datetime.now()
    formatted_now = formats.date_format(now, "TIME_FORMAT")
    formatted_date = formats.date_format(now, "DATE_FORMAT")
    
    #regex preps for fun and profit
    greet = re.compile('[Hh](i|ey|ello)')
    name = re.compile('(.*)([Yy]our ){0,1}name') #this is tricky but could be radically improved...
    time = re.compile('(([Ww]hat ){0,1}time is it(\?){0,4})')
    date = re.compile("((.*)(('|i)s ){0,1}the date(\?){0,4})")

    if name.match(req):
        return 'My name is John'
    if greet.match(req):
        return 'Hi there'
    if time.match(req):
        resp = "It is now %s" % formatted_now
        return resp
    if date.match(req):
        resp = "It's %s" % formatted_date
        return resp
    else:
        resp = Response.objects.order_by('?')[0]
        return resp.response

def ajax_obot_aiml(request):
    """


    """
    #some helpful variables:
    now = datetime.datetime.now()
    formatted_now = formats.date_format(now, "TIME_FORMAT")
    formatted_date = formats.date_format(now, "DATE_FORMAT")
    #the request
    req = request.GET.get('msg', '')

    #loading AIML libs
    #where else can I do this?
    learning_root = getattr(settings, 'DJANGO_ROOT', '') + '/static/aiml/standard/'

    learning_files = [
        'std-botmaster.aiml', 
        'std-brain.aiml', 
        'std-dictionary.aiml', 
        'std-hello.aiml', 
        'std-gender.aiml', 
        'std-religion.aiml', 
        'std-sextalk.aiml', 
        'std-profile', 
        'std-srai.aiml', 
        'std-yesno.aiml',
        'std-65percent.aiml',
    ]

    #AIML Play, needs a lot of research/work:
    k = aiml.Kernel()

    #load up learnign files, because loading from within the XML isn't working:
    for file in learning_files:
        k.learn(learning_root + file)

    #formulate response:
    obot_response = k.respond(req)
    #if AIML doesn't get us something, tap into the random stuff above...
    if len(obot_response) == 0:
        new_response = _local_ajax_obot_response(req)
        return HttpResponse(new_response)
    else:
        #return HTML
        return HttpResponse(obot_response)

    