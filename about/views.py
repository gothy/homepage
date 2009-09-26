# -*- coding: utf-8 -*-
from models import Biocard
from about.forms import BiocardForm

from django.shortcuts import render_to_response
from django.core.urlresolvers import reverse
from django.contrib.auth.decorators import login_required
from django.http import Http404, HttpResponseRedirect

@login_required
def about_view(request):
    'About Me display view, shows first(it should be one?) Biocard found in db'
    try:
        card = Biocard.objects.order_by('id')[0]
    except Biocard.DoesNotExist:
        raise Http404

    return render_to_response(
        'about/about_me.html', 
        locals()
    )

@login_required
def about_edit_view(request):
    'About Me edit view'
    try:
        card = Biocard.objects.order_by('id')[0]
    except Biocard.DoesNotExist:
        raise Http404
    
    if request.method == 'POST': # If the form has been submitted...
        form = BiocardForm(request.POST) # A form bound to the POST data
        if form.is_valid(): # All validation rules pass
            # Process the data in form.cleaned_data
            card.first_name = form.cleaned_data['first_name']
            card.second_name = form.cleaned_data['second_name']
            card.last_name = form.cleaned_data['last_name']
            card.bio = form.cleaned_data['bio']
            card.phone = form.cleaned_data['phone']
            card.email = form.cleaned_data['email']
            card.jid = form.cleaned_data['jid']
            card.twitter = form.cleaned_data['twitter']
            card.save()
            return HttpResponseRedirect(reverse(about_view)) # Redirect after POST
    else:
        form = BiocardForm(instance=card)
    
    return render_to_response(
        'about/about_me_edit.html', 
        locals()
    )
