from django.shortcuts import render,redirect
from .models import *
from .forms import *
from property_front_end.models import contactmodel,Buy_Property,sell_property_model
import os
from django.contrib import messages
from django.http import HttpResponse
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login
# Create your views here.

def index(request):
    return render(request,'index.html')




def adminregis(request):
  if request.method=='POST':
      nm=request.POST.get('username')
      fm=request.POST.get('firstname')
      lm=request.POST.get('lastname')
      em=request.POST.get('email')
      ph=request.POST.get('phonenumber')
      ps=request.POST.get('password')
      cs = request.POST.get('confirmpassword')
      if ps==cs:
          obj = adminreg(username=nm, firstname=fm, lastname=lm, email=em, password=ps, phonenumber=ph,
                         confirmpassword=cs)
          obj.save()
          return redirect(adminregis)

      else:
           messages.success(request, 'password doesnt match')
           return redirect(adminregis)
  else:
      return render(request,'registeradmin.html')



def registerdisplay(request):
    data=adminreg.objects.all()
    return render(request,'admindisplay.html',{'data':data})

def editreg(request , dataid):
    data=adminreg.objects.get(id=dataid)
    print(data)
    return render(request,"editadmin.html",{'data':data})


def adminupdate(request,dataid):
    data=adminreg.objects.get(id=dataid)
    form=adminregform(request.POST,instance=data)
    form.save()
    return redirect(registerdisplay)


def admindelete(request,dataid):
    data=adminreg.objects.get(id=dataid)
    data.delete()
    return redirect(registerdisplay)




def category(request):
    if request.method=='POST':
        a=categoryform(request.POST,request.FILES)
        if a.is_valid():
            pt=a.cleaned_data['property_name']
            ap=a.cleaned_data['aboutproperty']
            im=a.cleaned_data['propertyimage']
            b=categorymodel(property_name=pt,aboutproperty=ap,propertyimage=im)
            b.save()
            return  redirect(displaycat)
        else:
            return HttpResponse('file upload failed')
    else:
        return render(request,'addcategory.html')


def displaycat(request):
    a=categorymodel.objects.all()
    li=[]
    name=[]
    about=[]
    id=[]
    for i in a:
        id1=i.id
        id.append(id1)
        path=i.propertyimage
        li.append(str(path).split('/')[-1])
        nm=i.property_name
        name.append(nm)
        dis=i.aboutproperty
        about.append(dis)
    mylist=zip(name,about,li,id)
    return render(request,'displaycategory.html',{'mylist':mylist})



def editcategory(request,id):
    prod= categorymodel.objects.get(id=id)
    li=str(prod.propertyimage).split('/')[-1]
    if request.method=='POST':
        if len(request.FILES) !=0:
            if len(prod.propertyimage)>0:
                os.remove(prod. propertyimage.path)
            prod.propertyimage= request.FILES['propertyimage']
        prod.property_name = request.POST.get('property_name')
        prod.aboutproperty=request.POST.get('aboutproperty')
        prod.save()
        return redirect(displaycat)

    context= {'prod':prod,'li':li}
    return render(request,'editcategory.html',context)



def deletecategory(request,id):
    prod=categorymodel.objects.get(id=id)
    if len(prod.propertyimage)>0:  #image delete
        os.remove(prod.propertyimage.path)
    prod.delete()
    return redirect(displaycat)



# property function



def property(request):
    if request.method=='POST':
        a=propertyform(request.POST,request.FILES)
        if a.is_valid():
            ct=a.cleaned_data["category"]
            pt=a.cleaned_data['property_place']
            pp=a.cleaned_data['property_price']
            pa=a.cleaned_data['property_address']
            im=a.cleaned_data['property_img']
            b=propertymodel(category=ct,property_place=pt,property_price=pp,property_address=pa,property_img=im)
            b.save()
            return  redirect(propertydisplay)
        else:
            return HttpResponse('file upload failed')
    else:
        return render(request,'addproperty.html')



def propertydisplay(request):
    a=propertymodel.objects.all()
    li=[]
    cat=[]
    price=[]
    address=[]
    id=[]
    place=[]
    for i in a:
        id1=i.id
        id.append(id1)
        path=i.property_img
        li.append(str(path).split('/')[-1])
        nm=i.category
        cat.append(nm)
        pri=i.property_price
        price.append(pri)
        add=i.property_address
        address.append(add)
        pla=i.property_place
        place.append(pla)
    mylist=zip(cat,place,address,price,li,id)
    return render(request,'displayproperty.html',{'mylist':mylist})



def editproperty(request,id):
    prod= propertymodel.objects.get(id=id)
    li=str(prod.property_img).split('/')[-1]
    if request.method=='POST':
        if len(request.FILES) !=0:
            if len(prod.property_img)>0:
                os.remove(prod.property_img.path)
            prod.property_img= request.FILES['property_img']
        prod.category = request.POST.get('category')
        prod.property_place=request.POST.get('property_place')
        prod.property_address = request.POST.get('property_address')
        prod.property_price = request.POST.get('property_price')
        prod.save()
        return redirect(propertydisplay)

    context= {'prod':prod,'li':li}
    return render(request,'editproperty.html',context)



def deleteproperty(request,id):
    prod=propertymodel.objects.get(id=id)
    if len(prod.property_img)>0:  #image delete
        os.remove(prod.property_img.path)
    prod.delete()
    return redirect(propertydisplay)


def display_buy_property(request):
    a=Buy_Property.objects.all()
    concontact=[]
    conemail=[]
    conname=[]
    conphone=[]
    conbudget=[]
    id = []
    for i in a:
        id1 = i.id
        id.append(id1)
        nm=i.name
        conname.append(nm)
        dis=i.contact
        concontact.append(dis)
        em=i.email
        conemail.append(em)
        sub=i.phone
        conphone.append(sub)
        bud=i.budget
        conbudget.append(bud)
    mylist=zip(conname,conemail,conphone,concontact,conbudget,id)
    return render(request,'displaybuyproperty.html',{'mylist':mylist})


def delete_buy_property(request,id):
    prod=Buy_Property.objects.get(id=id)
    prod.delete()
    return redirect(display_buy_property)






def display_contactus(request):
    a=contactmodel.objects.all()
    emaildis=[]
    namedis=[]
    messagedis=[]
    subjectdis=[]
    id = []

    for i in a:
        id1 = i.id
        id.append(id1)
        nm=i.name
        namedis.append(nm)
        dis=i.message
        messagedis.append(dis)
        em=i.email
        emaildis.append(em)
        sub=i.subject
        subjectdis.append(sub)
    mylist=zip(namedis,emaildis,subjectdis,messagedis,id)
    return render(request,'displaycontactus.html',{'mylist':mylist})


def delete_contactus(request,id):
    prod=contactmodel.objects.get(id=id)
    prod.delete()
    return redirect(display_contactus)


def adminlog(request):
    if request.method=="POST":
        username_reg=request.POST.get('username')
        pasword_reg=request.POST.get('password')

        if User.objects.filter(username__contains=username_reg).exists():
            user=authenticate(username=username_reg,password=pasword_reg)
            if user is not None:
                login(request,user)
                request.session['username']=username_reg
                request.session['password']=pasword_reg
                return redirect(index)
            else:
                return redirect(adminlog)
        else:
            return redirect(adminlog)

    return render(request,'adminlogin.html')


def sellerpropertydisplay(request):
    a=sell_property_model.objects.all()
    li=[]
    name=[]
    numb=[]
    type=[]
    location=[]
    built=[]
    furnish=[]
    id=[]
    for i in a:
        id1=i.id
        id.append(id1)
        path=i.property_image
        li.append(str(path).split('/')[-1])
        nm=i.fullname
        name.append(nm)
        num=i.number
        numb.append(num)
        ty=i.propertytype
        type.append(ty)
        pla=i.propertylocation
        location.append(pla)
        bul= i.yearbuilt
        built.append(bul)
        fu = i.furnish
        furnish.append(fu)
    mylist=zip(name,numb,location,type,built,furnish,li,id)
    return render(request,'displaypropertysell.html',{'mylist':mylist})