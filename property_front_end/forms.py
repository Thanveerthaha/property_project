from django import forms
from .models import *


class Buy_Property_form(forms.Form):
    name = forms.CharField(max_length=20)
    phone = forms.CharField(max_length=20)
    email = forms.EmailField()
    budget = forms.CharField(max_length=30)
    contact = forms.CharField(max_length=20)


class sellpropertyform(forms.Form):
    fullname = forms.CharField(max_length=20)
    number=forms.IntegerField()
    propertytype=forms.CharField(max_length=30)
    propertylocation=forms.CharField(max_length=50)
    yearbuilt=forms.CharField(max_length=20)
    furnish=forms.CharField(max_length=30)
    property_image=forms.FileField()
