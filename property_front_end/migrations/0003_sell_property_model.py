# Generated by Django 4.2.4 on 2023-08-24 13:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('property_front_end', '0002_contactmodel'),
    ]

    operations = [
        migrations.CreateModel(
            name='sell_property_model',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fullname', models.CharField(max_length=20)),
                ('number', models.IntegerField()),
                ('propertytype', models.CharField(max_length=30)),
                ('propertylocation', models.CharField(max_length=50)),
                ('yearbuilt', models.CharField(max_length=20)),
                ('furnish', models.CharField(max_length=30)),
                ('property_image', models.FileField(upload_to='seller_property')),
            ],
        ),
    ]