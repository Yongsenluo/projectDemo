# Generated by Django 4.0.5 on 2022-08-11 00:00

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('attractionApp', '0008_alter_regionmodels_regionname'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='attractionmodels',
            name='attractionImg',
        ),
    ]
