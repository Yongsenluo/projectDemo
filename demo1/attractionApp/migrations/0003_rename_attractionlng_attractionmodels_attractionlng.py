# Generated by Django 4.0.5 on 2022-07-26 16:39

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('attractionApp', '0002_citymodels_cityregion'),
    ]

    operations = [
        migrations.RenameField(
            model_name='attractionmodels',
            old_name='attractionlng',
            new_name='attractionLng',
        ),
    ]
