from django.conf.urls.defaults import *

import views

urlpatterns = patterns('',
    (r'^$', views.about_view),
    (r'^edit/$', views.about_edit_view),
)
