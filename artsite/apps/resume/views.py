import json
from datetime import datetime
from django.core.cache import cache
from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404, render_to_response
from django import template
from models import Resume
from sorl.thumbnail import get_thumbnail


def resume_main(request):
    resume = get_object_or_404(Resume)
    return render(request, "resume/index.html",{
        'resume': resume
    })