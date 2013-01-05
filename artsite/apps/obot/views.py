from django.core import serializers
from django.shortcuts import render
from django.http import Http404, HttpResponse
from models import Response
 

def ajax_obot_response(request):
    """
    Returns what?

    returns: JSON
    """

    resp = Response.objects.order_by('?')[0]
    return HttpResponse(resp.response, mimetype='application/json')
