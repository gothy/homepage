# -*- coding: utf-8 -*-
from models import Biocard

from django.shortcuts import render_to_response
from django.contrib.auth.decorators import login_required
from django.http import Http404

@login_required
def about_view(request):
    'About Me display view, shows first(it should be one?) Biocard found in db'
    try:
        card = Biocard.objects.order_by('id')[0]
    except Biocard.DoesNotExist:
        raise Http404

    return render_to_response('about/about_me.html', locals())