import json
from datetime import datetime
from django.core.cache import cache
from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404, render_to_response
from django import template
from models import Category, Work, Link
from sorl.thumbnail import get_thumbnail

def home(request):
    categories = Category.objects.all()
    return render(request, "home.html",{
        'categories': categories
    })


def category_landing(request, category_slug):
    category = get_object_or_404(Category, slug=category_slug)
    works = Work.objects.filter(category=category)
    return render(request, "gallery/category_landing.html",{
        'category': category, 'works': works
    })
    #return 'gallery/category_landing.html', {'category': category, 'series': series}
                

def work_landing(request, category_slug, work_slug):
    category = get_object_or_404(Category, slug=category_slug)
    work = get_object_or_404(Work, slug=work_slug)
    return render(request, "gallery/work_landing.html",{
        'category': category, 'work': work
    })
    #return 'gallery/work_landing.html', {'category': category, 'series': series, 'work': work}

def links(request):
    links = Link.objects.all()
    return render(request, "gallery/links.html",{
        'links': links
    })