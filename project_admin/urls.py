from django.urls import path
from .views import *


urlpatterns = [
path('index/',index,name='index'),
path('registeradmin/',adminregis,name='adminregis'),
path('admindisplay/',registerdisplay,name='registerdisplay'),
path('editreg/<int:dataid>',editreg,name='editreg'),
path('adminupdate/<int:dataid>',adminupdate,name='adminupdate'),
path('admindelete/<int:dataid>',admindelete,name='admindelete'),

path('addcategory/',category,name='category'),
path('displaycategory/',displaycat,name='displaycat'),
path('editcategory/<int:id>',editcategory),
path('deletecategory/<int:id>',deletecategory),



path('addproperty/',property,name='property'),
path('displayproperty/',propertydisplay,name='propertydisplay'),
path('editproperty/<int:id>',editproperty,name='editproperty'),
path('deleteproperty/<int:id>',deleteproperty,name='deleteproperty'),


path('display_buy_property/',display_buy_property,name="display_buy_property"),
path('delete_buy_property/<int:id>',delete_buy_property,name='delete_buy_property'),

path('displaycontactus/',display_contactus,name="display_contactus"),
path('delete_contactus/<int:id>',delete_contactus,name='delete_contactus'),

path('adminlogin/',adminlog),

path('displaypropertyseller/',sellerpropertydisplay,name="sellerpropertydisplay"),


]
