from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class UserInformation(models.Model):
    # Information about User
    userInformation_id = models.AutoField(verbose_name="userInformation_id", primary_key=True)
    user = models.OneToOneField( verbose_name="user", to=User, on_delete=models.CASCADE)
    count_routes = models.IntegerField(verbose_name="how many routes post", default=0)
    count_likes = models.IntegerField(verbose_name="how many routes like",default=0)
    user_img = models.ImageField(verbose_name="user_img",upload_to="upload/user/",default='/media/upload/user/home.jpg')
    

