# Generated by Django 4.0.5 on 2022-08-02 14:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('routeApp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='bigroutemodels',
            name='routeDay',
            field=models.IntegerField(default=0, verbose_name='route days'),
        ),
    ]