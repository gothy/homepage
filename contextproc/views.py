# -*- coding: utf-8 -*-

from django.template import RequestContext
from django.shortcuts import render_to_response

def settings_proc_view(request):
    'test view to check processor with django.conf.settings in context'
    return render_to_response(
        'tests/settings_context_test.html', 
        {}, 
        context_instance=RequestContext(request)
    )
