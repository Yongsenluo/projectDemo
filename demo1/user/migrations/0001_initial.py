# Generated by Django 4.0.5 on 2022-07-25 12:51

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='UserInformation',
            fields=[
                ('userInformation_id', models.AutoField(primary_key=True, serialize=False, verbose_name='userInformation_id')),
                ('count_routes', models.IntegerField(default=0, verbose_name='how many routes post')),
                ('count_likes', models.IntegerField(default=0, verbose_name='how many routes like')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='user')),
            ],
        ),
    ]
