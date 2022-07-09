from wsgiref.simple_server import demo_app
from django.urls import path
from .import views

app_name = 'demo_app'

urlpatterns = [

    path('', views.index, name='index'),
    path('home', views.home, name='home'),
]
