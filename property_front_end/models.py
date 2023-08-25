from django.db import models

# Create your models here.


class Buy_Property(models.Model):
    name=models.CharField(max_length=20)
    phone=models.CharField(max_length=10)
    email=models.EmailField()
    budget=models.CharField(max_length=30)
    contact=models.CharField(max_length=10)

class contactmodel(models.Model):
    email=models.EmailField()
    name=models.CharField(max_length=20)
    message=models.CharField(max_length=250)
    subject=models.CharField(max_length=100)


class sell_property_model(models.Model):
    fullname = models.CharField(max_length=20)
    number=models.IntegerField()
    propertytype=models.CharField(max_length=30)
    propertylocation=models.CharField(max_length=50)
    yearbuilt=models.CharField(max_length=20)
    furnish=models.CharField(max_length=30)
    property_image=models.FileField(upload_to='seller_property')