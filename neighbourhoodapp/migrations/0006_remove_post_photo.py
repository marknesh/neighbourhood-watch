# Generated by Django 3.0.4 on 2020-03-26 16:13

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('neighbourhoodapp', '0005_auto_20200326_1744'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='photo',
        ),
    ]