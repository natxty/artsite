from django.conf import settings
from django.contrib import admin
from django.conf.urls import url, include
from django.urls import path
from django.conf.urls.static import static
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
# from django.views.generic.simple import redirect_to, direct_to_template
from django.views.generic import TemplateView

from artsite.apps.blog.views import * 
from artsite.apps.gallery.views import * 
from artsite.apps.resume.views import * 
from artsite.apps.obot.views import *


# See: https://docs.djangoproject.com/en/dev/ref/contrib/admin/#hooking-adminsite-instances-into-your-urlconf
admin.autodiscover()


# See: https://docs.djangoproject.com/en/dev/topics/http/urls/
urlpatterns = [
    # Admin panel and documentation:
    #url(r'^admin_tools/', include('admin_tools.urls')),
    url(r'^admin/order/(?P<category_slug>[\w-]+)/$', category_admin),
    url(r'^admin/reorder/$', reorder_datatypes),
    url(r'^admin/doc/', include('django.contrib.admindocs.urls')),
    url(r'^admin/', admin.site.urls),

    #contact
    url(r'^contact/', contact),
    url(r'^thanks/',  TemplateView.as_view(template_name='contact/thanks.html')),

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
    url(r'^chat/$', TemplateView.as_view(template_name='chat.html')),

    #lab-0
    url(r'^lab/$', TemplateView.as_view(template_name='lab.html')),

    #flatpages:
    path('pages/', include('django.contrib.flatpages.urls')),

	#gallery urls
    url(r'^$', home),
    #(r'^$', redirect_to, {'url': '/large-works/'} ),
    url(r'^(?P<category_slug>[\w-]+)/$', category_landing),
    url(r'^order/(?P<category_slug>[\w-]+)/$', category_admin),
    url(r'^(?P<category_slug>[\w-]+)/(?P<work_slug>[\w-]+)/$', work_landing),
]

#media urls
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
urlpatterns += staticfiles_urlpatterns()

#static urls
# urlpatterns = [
#     url(r'^static/(?P<path>.*)$', 'django.views.static.serve', {'document_root': settings.STATICFILES_DIRS[0]}),
# ] + urlpatterns
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

# debug toolbar:
if settings.DEBUG:
    import debug_toolbar

    urlpatterns += [
        path('__debug__/', include(debug_toolbar.urls)),
    ]
