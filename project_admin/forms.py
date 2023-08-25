from django import forms
from .models import *




class adminregform(forms.ModelForm):  #table
    class Meta:
        model=adminreg
        fields="__all__"


class categoryform(forms.Form):
    property_name=forms.CharField(max_length=20)
    aboutproperty=forms.CharField(max_length=200)
    propertyimage=forms.FileField()


class propertyform(forms.Form):
    category=forms.CharField(max_length=20)
    property_img=forms.FileField()
    property_place=forms.CharField(max_length=20)
    property_price=forms.IntegerField()
    property_address=forms.CharField(max_length=100)