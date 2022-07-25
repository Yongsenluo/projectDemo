import turtle
from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class UserInformation(models.Model):
    # 关于user的资料
    userInformation_id = models.AutoField(verbose_name="userInformation_id", primary_key=True)
    user = models.OneToOneField( verbose_name="user", to=User, on_delete=models.CASCADE)
    count_routes = models.IntegerField(verbose_name="how many routes post", default=0)
    count_likes = models.IntegerField(verbose_name="how many routes like",default=0)
    

