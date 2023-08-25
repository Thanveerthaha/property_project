from django.db import models

# Create your models here.
from django.contrib.auth.models import User


class adminreg(models.Model):
    username=models.CharField(max_length=20)
    firstname=models.CharField(max_length=20)
    lastname=models.CharField(max_length=20)
    email=models.EmailField()
    phonenumber=models.CharField(max_length=10)
    password=models.CharField(max_length=20)
    confirmpassword=models.CharField(max_length=20)



class categorymodel(models.Model):
    property_name=models.CharField(max_length=20)
    aboutproperty=models.CharField(max_length=100)
    propertyimage=models.FileField(upload_to='category_image')


class propertymodel(models.Model):
    category=models.CharField(max_length=20)
    property_img=models.FileField(upload_to='product_image')
    property_place=models.CharField(max_length=20)
    property_price=models.IntegerField()
    property_address=models.CharField(max_length=100)