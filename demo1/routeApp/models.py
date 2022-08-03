from django.db import models
from django.contrib.auth.models import User
from attractionApp.models import cityModels,attractionModels
# Create your models here.

class bigRouteModels(models.Model):
    routeId = models.AutoField(verbose_name="route id",primary_key=True)
    routeName = models.CharField(verbose_name="route name",max_length=128)
    routeDate = models.DateField(verbose_name="publish time",auto_now_add=True)
    routeUser =  models.ForeignKey(verbose_name="belong to which user", to=User, on_delete=models.CASCADE)
    routeImg = models.ImageField(verbose_name="route img",upload_to="upload/route/",default='/media/upload/user/home.jpg')
    routeDay = models.IntegerField(verbose_name="route days",default=0)
    
    routeLike = models.IntegerField(verbose_name="how many person liked", default=0)
    routeComment = models.IntegerField(verbose_name="how many person commented", default=0)
    
    class Meta:
        verbose_name_plural = "Big Route"

    def save(self, *args, **kwargs):
        if self.routeComment < 0:
            self.routeComment = 1
        super(bigRouteModels, self).save(*args, **kwargs)



class dayRouteModels(models.Model):
    dayRouteId = models.AutoField(verbose_name="day route id",primary_key=True)
    dayRouteUser =  models.ForeignKey(verbose_name="belong to which user", to=User, on_delete=models.CASCADE)
    dayRoutetoBigRoute = models.ForeignKey(verbose_name = "below to which big route",to=bigRouteModels,on_delete=models.CASCADE)
    dayRouteCity = models.ManyToManyField(cityModels)
    dayRouteAttraction = models.ManyToManyField(attractionModels)
    class Meta:
        verbose_name_plural = "Day Route"



class commentModels (models.Model):
    commentId = models.AutoField(verbose_name="comment id", primary_key=True)
    commentText = models.TextField(verbose_name="comment content")
    commentTime = models.DateTimeField(auto_now_add=True)
    commentUser = models.ForeignKey(verbose_name = "below which user",to=User, on_delete=models.CASCADE)
    commentRoute = models.ForeignKey(verbose_name="belong to which route", to=bigRouteModels, on_delete=models.CASCADE)

    def save(self, *args, **kwargs):
        if len(self.commenText) <= 0 or self.commentText.isspace():
            self.commentText = "invalid comment input"
        super(commentModels, self).save(*args, **kwargs)


class likeModels (models.Model):
    likeId = models.AutoField(verbose_name="like Id",primary_key=True)
    likeUser = models.ForeignKey(verbose_name="like poster id",to=User,on_delete=models.CASCADE)
    likeRoute =models.ForeignKey(verbose_name="like route id",to=bigRouteModels,on_delete=models.CASCADE)
    class Meta:
        verbose_name_plural = "like table"