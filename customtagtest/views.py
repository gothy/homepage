# -*- coding: utf-8 -*-
from homepage.about.models import Biocard

from django.shortcuts import render_to_response
from django.contrib.auth.decorators import login_required

@login_required
def test_view(request):
    'edit_in_admin tag test view'
    card = Biocard.objects.order_by('id')[0]

    return render_to_response(
        'tests/edit_in_admin_test.html', 
        locals()
    )