# Generated by Django 3.2.4 on 2021-06-05 12:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='images',
            field=models.ImageField(blank=True, upload_to='../image/photos/products'),
        ),
    ]
