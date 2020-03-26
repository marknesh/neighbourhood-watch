# Generated by Django 3.0.4 on 2020-03-26 14:44

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('neighbourhoodapp', '0004_delete_signupforms'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='User',
            new_name='Users',
        ),
        migrations.AlterField(
            model_name='business',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('photo', models.ImageField(upload_to='posted')),
                ('comment', models.CharField(max_length=300)),
                ('neighbourhood', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='neighbourhoodapp.Neighbourhood')),
            ],
        ),
    ]
