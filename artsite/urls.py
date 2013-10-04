from django.conf import settings
from django.contrib import admin
from django.conf.urls.defaults import *
from django.conf.urls.static import static
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.views.generic.simple import redirect_to, direct_to_template

from artsite.apps.blog.views import * 
from artsite.apps.gallery.views import * 
from artsite.apps.resume.views import * 
from artsite.apps.obot.views import * 


# See: https://docs.djangoproject.com/en/dev/ref/contrib/admin/#hooking-adminsite-instances-into-your-urlconf
admin.autodiscover()


# See: https://docs.djangoproject.com/en/dev/topics/http/urls/
urlpatterns = patterns('',
    # Admin panel and documentation:
    #url(r'^admin_tools/', include('admin_tools.urls')),
    url(r'^admin/order/(?P<category_slug>[\w-]+)/$', 'apps.gallery.views.category_admin'),
    url(r'^admin/reorder/$', 'apps.gallery.views.reorder_datatypes'),
    url(r'^admin/doc/', include('django.contrib.admindocs.urls')),
    url(r'^admin/', include(admin.site.urls)),

    #contact
    url(r'^contact/', 'apps.gallery.views.contact'),
    url(r'^thanks/',  direct_to_template, {'template': 'contact/thanks.html'}, name='thanks' ),

    #links/biblio
    url(r'^links/$', links),

    # blog urls
    url(r'^blog/$', blog_main), 
	url(r'^blog/post/(?P<post_id>\d+)/$', post_specific), 

    #pages:
    url(r'^resume/pdf/$', resume_pdf),
    url(r'^resume/$', resume_main), 

    # ajax request URLs for obot
    url(r'^obot/response/$', ajax_obot_response),
    url(r'^obot/aiml/$', ajax_obot_aiml),

    #big bot
    url(r'^chat/$', direct_to_template, {'template': 'chat.html'}, name='chat_with_john'),

    #lab-0
    url(r'^lab/$', direct_to_template, {'template': 'lab.html'}, name='the_lab'),

    #flatpages:
    ('^pages/', include('django.contrib.flatpages.urls')),  

	#gallery urls
    (r'^$', home),
    #(r'^$', redirect_to, {'url': '/large-works/'} ),
    url(r'^(?P<category_slug>[\w-]+)/$', category_landing),
    url(r'^order/(?P<category_slug>[\w-]+)/$', category_admin),
    url(r'^(?P<category_slug>[\w-]+)/(?P<work_slug>[\w-]+)/$', work_landing),

    

)

#media urls
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
urlpatterns += staticfiles_urlpatterns()

#static urls
urlpatterns = patterns('',
    (r'^static/(?P<path>.*)$', 'django.views.static.serve', {'document_root': settings.STATICFILES_DIRS[0]}),
) + urlpatterns
