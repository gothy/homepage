from django.conf.urls.defaults import *

from contextproc.views import settings_proc_view

urlpatterns = patterns('',
    (r'^', settings_proc_view),
)
