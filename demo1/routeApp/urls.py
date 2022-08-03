from django.urls import path
from .import views

app_name = 'routeApp'

urlpatterns = [
    path('createRoute/',views.createRoute,name="createRoute"),
]
