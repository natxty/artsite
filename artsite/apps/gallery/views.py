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

#for admin views:
from django.contrib.admin.views.decorators import staff_member_required




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
    works = Work.objects.filter(category=category).order_by('order')
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



#
# Admin View 
#

@staff_member_required
def category_admin(request, category_slug):
    category = get_object_or_404(Category, slug=category_slug)
    
    if request.method == "POST":
        def clean_id_list(id_list):
            clean_id_list = []
            for item in id_list:
                try:
                    clean_id_list.append(int(item))
                except ValueError:
                    pass
            return clean_id_list

        def update_works(id_list):
            clean_ids = clean_id_list(id_list)

            sorting_counter = 1
            for id in id_list:
                work_single = Work.objects.get(pk=id)
                work_single.order = sorting_counter
                work_single.save()
                sorting_counter += 1


        new_order = request.POST.getlist('work[]')
        update_works(new_order)

    works_list = Work.objects.filter(category=category).order_by('order')

    return render_to_response('gallery/category_admin.html', context_instance=RequestContext(request, {
        'category': category, 'works': works_list
    }))
    #return 'gallery/category_landing.html', {'category': category, 'series': series}


@staff_member_required
def reorder_datatypes(request):
    t = loader.get_template('admin/reorder.html')
    # can change what fields you can edit within the drag and drop items, like name
    DataTypeFormSet = modelformset_factory(DataType, extra = 0,
        fields=('display_name', 'code_name', 'order'))
    
    if request.method == "POST":
        formset = DataTypeFormSet(request.POST)
        
        if formset.is_valid():
            formset.save()
            # reset the order to what's been saved
            formset = DataTypeFormSet(queryset=DataType.objects.order_by('order'))
    else:        
        formset = DataTypeFormSet(queryset=DataType.objects.order_by('order'))
    
    c = Context({
        'title': 'Data Type Order',
        'formset': formset,
        # change this to the admin add link of the item you are reordering
        'new_item_url': reverse('admin:MyApp_datatype_add'),
    })
    
    return HttpResponse(t.render(c))




