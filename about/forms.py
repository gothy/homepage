# -*- coding: utf-8 -*-

from django import forms

from models import Biocard

class BiocardForm(forms.ModelForm):
    'form for Biocard model'
    
    class Meta:
        model = Biocard