# Generated by Django 2.2 on 2020-05-10 08:04

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0002_profiles_image'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='profiles',
            name='image',
        ),
    ]
