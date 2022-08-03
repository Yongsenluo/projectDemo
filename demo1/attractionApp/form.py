
from django import forms

from demo1.attractionApp.models import cityModels,attractionModels

class cityForm(forms.ModelForm):
    class Meta:
        cityModel = cityModels
        field =['cityName','cityRegion','cityTrueId']  

class attractionForm(forms.ModelForm):
    class Meta:
        cityModel = cityModels
        field = ['attractionName','attractionLat','attractionLng','attractionContent','attractionPostcode','attractionImg','attractionCategory','attractionCity','attractionTrueId']