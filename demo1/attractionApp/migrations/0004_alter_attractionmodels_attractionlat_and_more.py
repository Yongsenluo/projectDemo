# Generated by Django 4.0.5 on 2022-07-27 16:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('attractionApp', '0003_rename_attractionlng_attractionmodels_attractionlng'),
    ]

    operations = [
        migrations.AlterField(
            model_name='attractionmodels',
            name='attractionLat',
            field=models.CharField(max_length=50, verbose_name='attraction latitude'),
        ),
        migrations.AlterField(
            model_name='attractionmodels',
            name='attractionLng',
            field=models.CharField(max_length=50, verbose_name='attraction longtitude'),
        ),
    ]