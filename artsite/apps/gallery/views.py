import json
from datetime import datetime
from django.core.cache import cache
from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404, render_to_response, redirect
from django import template
from django.template import RequestContext
from models import Category, Work, Link
from sorl.thumbnail import get_thumbnail
from random import choice




def home(request):
    '''
    Home will show the first active category
    '''
    '''
    categories = Category.objects.all()
    works = Work.objects.filter(category=categories[0])
    category = categories[0]

    return render(request, "home.html",{
        'categories': categories, 'works': works, 'category': category,
    })
    '''

    '''
    Home will choose randomly from the categories and redirect to one of them...
    '''
    categories = Category.objects.all()
    elect = choice(categories)
    print elect.slug

    return redirect('/' + elect.slug + '/')


def category_landing(request, category_slug):
    category = get_object_or_404(Category, slug=category_slug)
    works = Work.objects.filter(category=category).order_by('order').reverse()
    return render(request, "gallery/category_landing.html",{
        'category': category, 'works': works
    })
    #return 'gallery/category_landing.html', {'category': category, 'series': series}
                

def work_landing(request, category_slug, work_slug):
    category = get_object_or_404(Category, slug=category_slug)
    work = get_object_or_404(Work, slug=work_slug)

    #next work:
    try:
        next = Work.objects.filter(category=category).filter(order__gt=work.order).order_by('order')[0:1].get()
    except Work.DoesNotExist:
        next = None

    #previous:  
    try:
        prev = Work.objects.filter(category=category).filter(order__lt=work.order).order_by('order')[0:1].reverse().get()
    except Work.DoesNotExist:
        prev = None


    return render(request, "gallery/work_landing.html",{
        'category': category, 'work': work, 'next': next, 'previous': prev,
    })
    #return 'gallery/work_landing.html', {'category': category, 'series': series, 'work': work}

def links(request):
    links = Link.objects.all()
    return render(request, "gallery/links.html",{
        'links': links
    })