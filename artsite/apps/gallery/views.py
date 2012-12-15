import json
from datetime import datetime
from django.core.cache import cache
from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404, render_to_response
from django import template
from models import Category, Series, Work
from sorl.thumbnail import get_thumbnail

def home(request):
    categories = Category.objects.all()
    return render(request, "home.html",{
        'categories': categories
    })


def category_landing(request, category_slug):
    category = get_object_or_404(Category, slug=category_slug)
    series = Series.objects.filter(category=category)
    return render(request, "gallery/category_landing.html",{
        'category': category, 'series': series
    })
    #return 'gallery/category_landing.html', {'category': category, 'series': series}

def series_landing(request, category_slug, series_slug):
    category = get_object_or_404(Category, slug=category_slug)
    series = get_object_or_404(Series, slug=series_slug)
    works = Work.objects.filter(series=series)
    return render(request, "gallery/series_landing.html",{
        'category': category, 'series': series, 'works': works
    })
    #return 'gallery/series_landing.html', {'category': category, 'series': series, 'works': works}
                

def work_landing(request, category_slug, series_slug, work_slug):
    category = get_object_or_404(Category, slug=category_slug)
    series = get_object_or_404(Series, slug=series_slug)
    work = get_object_or_404(Work, slug=work_slug)
    return render(request, "gallery/work_landing.html",{
        'category': category, 'series': series, 'work': work
    })
    #return 'gallery/work_landing.html', {'category': category, 'series': series, 'work': work}
