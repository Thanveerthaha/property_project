# Generated by Django 4.2.4 on 2023-08-19 13:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('project_admin', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='categorymodel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('property_name', models.CharField(max_length=20)),
                ('aboutproperty', models.CharField(max_length=100)),
                ('propertyimage', models.FileField(upload_to='category_image')),
            ],
        ),
    ]
