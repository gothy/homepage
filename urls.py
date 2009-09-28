# -*- coding: utf-8 -*-
import os
from django.conf import settings
from django.conf.urls.defaults import *

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    (r'^$', 'django.views.generic.simple.redirect_to', {'url': '/about/'}),
    (r'^about/', include('homepage.about.urls')),
    (r'^accounts/login/$', 'django.contrib.auth.views.login'),
    (r'^accounts/logout/$', 'django.contrib.auth.views.logout', 
        {'next_page':'/about/'}
    ),
    (r'^tests/contextproctest/$', include('homepage.contextproc.urls')),
    (r'^tests/customtagtest/$', 'homepage.customtagtest.views.test_view'),
    # Example:
    # (r'^homepage/', include('homepage.foo.urls')),

    # Uncomment the admin/doc line below and add 'django.contrib.admindocs' 
    # to INSTALLED_APPS to enable admin documentation:
    # (r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/(.*)', admin.site.root, name='admin'),
)

if settings.DEBUG:
    urlpatterns += patterns('',
        (r'^static/(?P<path>.*)$', 'django.views.static.serve', 
            {'document_root': os.path.join(settings.PROJECT_PATH, 'static')}
        ),
    )