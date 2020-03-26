# Generated by Django 3.0.4 on 2020-03-26 13:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('neighbourhoodapp', '0002_business_neighbourhood_user'),
    ]

    operations = [
        migrations.CreateModel(
            name='SignupForms',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.EmailField(help_text='Required', max_length=200)),
                ('first_name', models.CharField(help_text='Required', max_length=200)),
                ('last_name', models.CharField(help_text='Required', max_length=200)),
            ],
        ),
    ]
