# Generated by Django 2.2.6 on 2019-10-24 21:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0002_auto_20191025_0002'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='description',
            field=models.CharField(default='Generic sandals wear. Buy you will enjoy its durability for sure :)', max_length=1000),
        ),
    ]
