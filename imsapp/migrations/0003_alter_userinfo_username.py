# Generated by Django 4.2.5 on 2023-10-20 10:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('imsapp', '0002_buyerinfo_companyinfo_product_producttype_vendorinfo_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userinfo',
            name='username',
            field=models.CharField(max_length=200),
        ),
    ]
