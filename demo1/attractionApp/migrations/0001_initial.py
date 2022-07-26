# Generated by Django 4.0.5 on 2022-07-26 15:03

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='categoryModels',
            fields=[
                ('categoryId', models.AutoField(primary_key=True, serialize=False, verbose_name='category id')),
                ('categoryName', models.CharField(max_length=100, verbose_name='category name')),
                ('categoryLikes', models.IntegerField(default=0, verbose_name='how many people like this category')),
            ],
        ),
        migrations.CreateModel(
            name='cityModels',
            fields=[
                ('cityId', models.AutoField(primary_key=True, serialize=False, verbose_name='city id')),
                ('cityName', models.CharField(max_length=128, verbose_name='city name')),
                ('cityLikes', models.IntegerField(default=0, verbose_name='how many people like this city')),
            ],
        ),
        migrations.CreateModel(
            name='regionModels',
            fields=[
                ('regionId', models.AutoField(primary_key=True, serialize=False, verbose_name='region id')),
                ('regionName', models.CharField(choices=[('E', 'England'), ('S', 'Scotland'), ('W', 'Wales')], max_length=3, verbose_name='region name')),
                ('regionLikes', models.IntegerField(default=0, verbose_name='how many people like this region')),
            ],
        ),
        migrations.CreateModel(
            name='attractionModels',
            fields=[
                ('attractionId', models.AutoField(primary_key=True, serialize=False, verbose_name='attraction id')),
                ('attractionName', models.CharField(max_length=128, verbose_name='attraction name')),
                ('attractionLat', models.DecimalField(decimal_places=6, max_digits=10, verbose_name='attraction latitude')),
                ('attractionlng', models.DecimalField(decimal_places=6, max_digits=10, verbose_name='attraction longtitude')),
                ('attractionContent', models.TextField(verbose_name='attraction_content')),
                ('attractionPostcode', models.CharField(max_length=128, verbose_name='attraction_postcode')),
                ('attractionImg', models.ImageField(upload_to='upload/attraction/', verbose_name='attraction_img')),
                ('attractionLikes', models.IntegerField(default=0, verbose_name='how many people love this attraction')),
                ('attractionCategory', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='attractionApp.categorymodels', verbose_name='which category')),
                ('attractionCity', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='attractionApp.citymodels', verbose_name='which city is it')),
            ],
        ),
    ]
