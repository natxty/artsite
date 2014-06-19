import re, os, datetime, aiml
from random import randint, choice
from django.conf import settings
from django.utils import formats
from django.core import serializers
from django.shortcuts import render
from django.http import Http404, HttpResponse
from models import Response, Log




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

    resp = Response.objects.order_by('?')[0]
    return resp.response


def ajax_obot_aiml(request):
    """


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
    show = re.compile('((.*)([Gg]allery(\s){0,1}){0,1}[Ss]how)')
    gallery = re.compile('(.*) (represented by|(show|have work) in) a [Gg]aller(y|ies)')


    #the request
    req = request.GET.get('msg', '')

    # save the chat to the Log
    _log = Log(author = 'User', content = req)
    _log.save()

    #loading AIML libs
    #where else can I do this?
    learning_root = getattr(settings, 'DJANGO_ROOT', '') + '/static/aiml/standard/'

    learning_files = [
        'std-65percent.aiml',
        'std-atomic.aiml',
        'std-botmaster.aiml',
        'std-brain.aiml',
        'std-dictionary.aiml',
        'std-hello.aiml',
        'std-inactivity',
        'std-gender.aiml',
        'std-religion.aiml',
        'std-sextalk.aiml',
        'std-sports.aiml'
        'std-politics.aiml',
        'std-profile',
        'std-srai.aiml',
        'std-yesno.aiml',
    ]

    #AIML Play, needs a lot of research/work:
    k = aiml.Kernel()

    #load up learnign files, because loading from within the XML isn't working:
    for file in learning_files:
        k.learn(learning_root + file)

    if gallery.match(req):
        response = "Why, yes. I often have work in Pierogi Gallery, in Brooklyn"
    elif show.match(req):
        response = "Hey! You're at my show, I think. The Machine and the Ghost."
    elif name.match(req):
        response = 'My name is John'
    elif greet.match(req):
        response = 'Hi there'
    elif time.match(req):
       response = "It is now %s %s" % (formatted_now, randTimeResponse() )
    elif date.match(req):
        response = "It's %s" % formatted_date
    else:
        #formulate response:
        obot_response = k.respond(req)
        #if AIML doesn't get us something, tap into the random stuff above...
        if len(obot_response) == 0:
            response = _local_ajax_obot_response(req)
        else:
            #return HTML
            response = obot_response

    # save the chat to the Log
    _log = Log(author = 'Obot', content = response)
    _log.save()

    #return
    return HttpResponse(response)


def randTimeResponse():
    time = ['but not in this time zone.', 'in California, where my heart is.', '... but not for long', 'but for me, it\'s always now', 'but what time is it on the sun?', 'but why do you want to know?', '- do you have somewhere else to be?']
    return choice(time)







