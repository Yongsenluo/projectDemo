# Generated by Django 4.0.5 on 2022-08-11 00:01

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('attractionApp', '0009_remove_attractionmodels_attractionimg'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='attractionmodels',
            name='attractionContent',
        ),
    ]
