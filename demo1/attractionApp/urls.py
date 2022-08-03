from django.contrib.auth import views as authView
from django.urls import path
from .import views

app_name = 'attractionApp'

urlpatterns = [ 
    path('createAttraction/',views.createAttraction,name="createAttraction"),
    path('geocoding/',views.geocoding,name='geocoding') ,
]
