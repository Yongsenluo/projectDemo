
from tabnanny import verbose
from django.db import models

# Create your models here.
#关于景点，城市的models
class regionModels(models.Model):
    REGION_NAME =(
        ('E','England'),
        ('S','Scotland'),
        ('W','Wales'),
    )
    regionId = models.AutoField(verbose_name="region id",primary_key=True)
    #choose a region from REGION_NAME
    regionName = models.CharField(verbose_name = "region name",max_length=3,choices=REGION_NAME)
    regionLikes = models.IntegerField(verbose_name="how many people like this region",default=0)
    
    class Meta:
        verbose_name_plural = "region"

class cityModels(models.Model):
    cityId = models.AutoField(verbose_name="city id",primary_key=True)
    cityName = models.CharField(verbose_name="city name",max_length=128)
    cityLikes = models.IntegerField(verbose_name="how many people like this city",default=0)
    cityRegion = models.ForeignKey(verbose_name="city region", to=regionModels,on_delete=models.CASCADE, default=None)

    class Meta:
        verbose_name_plural = "city"

class categoryModels(models.Model):
    categoryId = models.AutoField(verbose_name="category id",primary_key=True)
    categoryName = models.CharField(verbose_name="category name", max_length = 100)
    categoryLikes = models.IntegerField(verbose_name="how many people like this category",default=0)

    class Meta:
        verbose_name_plural = "category"

class attractionModels(models.Model):
    attractionId = models.AutoField(verbose_name="attraction id",primary_key=True)
    attractionName = models.CharField(verbose_name="attraction name", max_length=128)
    attractionLat = models.CharField( verbose_name="attraction latitude", max_length=50)
    attractionLng = models.CharField(verbose_name="attraction longtitude",max_length=50)
    attractionContent = models.TextField(verbose_name = "attraction_content")
    attractionPostcode = models.CharField(verbose_name="attraction_postcode",max_length=128)
    attractionImg = models.ImageField(verbose_name="attraction_img",upload_to= "upload/attraction/")
    attractionLikes = models.IntegerField(verbose_name="how many people love this attraction",default=0)
    attractionCategory = models.ForeignKey(verbose_name="which category",to=categoryModels,on_delete=models.CASCADE)
    attractionCity = models.ForeignKey(verbose_name="which city is it",to=cityModels,on_delete=models.CASCADE)

    class Meta:
        verbose_name_plural = "attraction"



