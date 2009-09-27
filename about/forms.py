# -*- coding: utf-8 -*-

from django import forms

from models import Biocard

class BiocardForm(forms.ModelForm):
    'form for Biocard model'
    first_name = forms.CharField(max_length=100, required=True)
    last_name = forms.CharField(max_length=100, required=True)
    phone = forms.CharField(max_length=15, required=False, label="Phone number")
    email = forms.EmailField(max_length=100, required=False, label="Email address")
    
    class Meta:
        model = Biocard
BiocardForm.base_fields.keyOrder.reverse() #reverse fields, comment to remove