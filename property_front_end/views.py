from django.shortcuts import render,redirect
from project_admin.models import categorymodel,propertymodel
from .models import *
from .forms import *
import os
from django.contrib import messages
from django.http import HttpResponse
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth import authenticate

# Create your views here.



def index(request):
    return render(request,'homepage.html')

def about(request):
    return render(request,'about.html')

def contact(request):
    return render(request,'contactus.html')

def services(request):
    return render(request,'services.html')

def properties(request):
    return render(request,'properties.html')

def category_detail(request):

        a = categorymodel.objects.all()
        li = []
        name = []
        about = []

        for i in a:
            path = i.propertyimage
            li.append(str(path).split('/')[-1])
            nm = i.property_name
            name.append(nm)
            dis = i.aboutproperty
            about.append(dis)
        mylist = zip(li,name,about)
        return render(request, 'categories.html', {'mylist': mylist})


def property_detail(request,category):
    properties=propertymodel.objects.filter(category=category)
    li = []
    name = []
    place = []
    address=[]
    id=[]
    for i in properties:
        id1 = i.id
        id.append(id1)
        path = i.property_img
        li.append(str(path).split('/')[-1])
        nm = i.property_place
        name.append(nm)
        dis = i.property_price
        place.append(dis)
        add = i.property_address
        address.append(add)
    mylist = zip(li, name, place,address,id)
    return render(request,'property_details.html',{'mylist':mylist})


def detail_card(request,id):
    prop= propertymodel.objects.get(id=id)
    if request.method == 'POST':
                        a = Buy_Property_form(request.POST)
                        if a.is_valid():
                            nm = a.cleaned_data['name']
                            em = a.cleaned_data['email']
                            ph = a.cleaned_data['phone']
                            bt = a.cleaned_data['budget']
                            ct = a.cleaned_data['contact']
                            b = Buy_Property(name=nm, email=em, phone=ph,budget=bt,contact=ct)
                            b.save()
                            return render(request,'success.html')
                        else:
                            return HttpResponse("registration failed")
    return render(request,'details.html',{'prop':prop})





def success(request):
    return render(request,'success.html')



def contact(request):
  if request.method=='POST':
      nm=request.POST.get('name')
      em=request.POST.get('email')
      mg=request.POST.get('message')
      sb=request.POST.get('subject')
      obj = contactmodel(name=nm, subject=sb, message=mg, email=em)
      obj.save()
      messages.success(request, 'message send success')
      return redirect(contact)

  else:
      return render(request,'contactus.html')



def sellproperty(request):
    if request.method == 'POST':
            a = sellpropertyform(request.POST, request.FILES)
            if a.is_valid():
                fn = a.cleaned_data["fullname"]
                pt = a.cleaned_data['propertytype']
                pl = a.cleaned_data['propertylocation']
                img = a.cleaned_data['property_image']
                num= a.cleaned_data['number']
                yb= a.cleaned_data['yearbuilt']
                fur = a.cleaned_data['furnish']
                b = sell_property_model(fullname=fn,propertytype=pt,propertylocation=pl,property_image=img,number=num,yearbuilt=yb,furnish=fur)
                b.save()
                return render(request,'propertysellsuccess.html')
            else:
                return HttpResponse('file upload failed')
    else:

        return render(request,'sellproperty.html')