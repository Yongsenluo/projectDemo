# Generated by Django 4.0.5 on 2022-07-26 15:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='userinformation',
            name='user_img',
            field=models.ImageField(default='/media/upload/user/home.jpg', upload_to='upload/user/', verbose_name='user_img'),
        ),
    ]