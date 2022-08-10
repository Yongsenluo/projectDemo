from unicodedata import name
from django.urls import path
from .import views

app_name = 'routeApp'

urlpatterns = [
    path('createRoute/',views.createRoute,name="createRoute"),
    path('createDayRoute/id=<bigRoute_id>',views.createDayRoute,name="createDayRoute"),
    path('dayRouteTem/dayRouteId=<dayRoute_id>',views.dayRouteDetail,name="dayRouteDetail"),
    path('addCity/',views.addCity,name="addCityMethod"),
    path('addAttraction/',views.addAttraction2,name="addAttractionMethod"),
    path('everyDayMap/',views.everyDayMap,name='everyDayMap'),
]
