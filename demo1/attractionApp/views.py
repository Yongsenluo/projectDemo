from ast import If
from ctypes.wintypes import PINT
from dataclasses import field
import http
import imp
import re
from traceback import print_tb
from unicodedata import category
from django.http import HttpResponse
from django.shortcuts import redirect, render

from decimal import Decimal
from urllib.parse import urlencode
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import redirect


from django.http import HttpResponse
from django.shortcuts import render
from pymysql import NULL
from .models import attractionModels, categoryModels, cityModels, regionModels
import urllib
import json
import urllib.request


# Create your views here.


def createAttraction(requests):
    if requests.method == 'POST':

        return HttpResponse('create successful')
    return render(requests, 'createAttraction.html')


@csrf_exempt
def map(requests):
    if requests.method == 'POST':
        lat = requests.POST.get('lat')
        lng = requests.POST.get('lng')
        lat = Decimal(lat)
        lng = Decimal(lng)
        context = [lat, lng]
        return HttpResponse(lat)
    return render(requests, 'map2.html')


@csrf_exempt
def geocoding(requests):
    if requests.method == 'POST':
        #try:
            address = requests.POST.get('address')
            json = gecodingAddress(address)
            print(json)
            placeId = json['results'][0].get("place_id")
            placeType = json['results'][0].get("types")
            json2 = placeJson(placeId)
            latLngContext  ={
                'json':json2,
                'lat': json['results'][0].get("geometry")['location']['lat'],
                'lng': json['results'][0].get("geometry")['location']['lng']
            }
            print(latLngContext)
            for pt in placeType:
                if pt == "locality":
                    print("this is a city")
                    cityIsNotExit = cityModels.objects.filter(cityTrueId = placeId)
                    if cityIsNotExit.exists():
                        print("city is exist")
     
                    else:
                        createCity(address)

                if pt == "political":
                    print("this is a city")
                    cityIsNotExit = cityModels.objects.filter(cityTrueId = placeId)
                    if cityIsNotExit.exists():
                        print("city is exit")

                    else:
                        createCity(address)
                return render(requests,'testMap.html',{'LatLng': latLngContext})
            placeIdExit = attractionModels.objects.filter(
            attractionTrueId=placeId)
            print(placeId)
            if placeIdExit.exists():
                print("存在")
            else:
                print("不存在，创建")
                createAttraction(json)
            return render(requests,'testMap.html',{'LatLng': latLngContext})
        #except:
            return HttpResponse("this attraction not exit")
            
    return render(requests, "testMap.html")



# method od create attraction
def createAttraction(attractionJson):
    attractionId = attractionJson['results'][0].get("place_id")
    print(attractionId)
    detailsJson = placeJson(attractionId)
    print(detailsJson['result']['name'])
    name = detailsJson['result']['name']
    lat = attractionJson['results'][0].get("geometry")['location']['lat']
    lng = attractionJson['results'][0].get("geometry")['location']['lng']
    test = attractionJson['results'][0].get("address_components")
    attractionCity = searchSomethingInAddress(test,'postal_town')

    #print(detailsJson['result']['types'])
    postcode = searchSomethingInAddress(test,'postal_code')
    attractionCategory = detailsJson['result']['types'][0]
    #判断该category是否存在？
    attractionCategoryExit = categoryModels.objects.filter(categoryName = attractionCategory)

    if attractionCategoryExit.exists():
        print("category exit")
    else:
        print("category not exit, create")
        attractionCategory = categoryModels(categoryName = attractionCategory)
        attractionCategory.save()


    #判断这个city是否存在？
    attractionCityExit = cityModels.objects.filter(cityName=attractionCity)
    if attractionCityExit.exists():
        print("city exit")
    else:
        print("city not exit, create city...")
        createCity(attractionCity)

    print(cityModels.objects.get(cityName = attractionCity))

    # start to create attraction object
    attractionObject = attractionModels(
        attractionName = name,
        attractionLat = lat,
        attractionLng = lng,
        attractionPostcode = postcode,
        attractionCategory = categoryModels.objects.get(categoryName = attractionCategory),
        attractionCity = cityModels.objects.get(cityName = attractionCity),
        attractionTrueId = attractionId
    )
    attractionObject.save()
    return attractionObject

# the method of create city, return city object
def createCity(cityName):
    print(cityName)
    cityJson = gecodingAddress(cityName)
    test = cityJson['results'][0].get("address_components")
    print(test)
    name = searchSomethingInAddress(test,"locality")
    # 但是有的城市不是用locality的，是用 political
    if len(name) == 0:
        name = searchSomethingInAddress(test,"administrative_area_level_1")

    cityId = cityJson['results'][0].get("place_id")
    region = searchSomethingInAddress(test,"administrative_area_level_1")
    cityRegion1 = regionModels.objects.filter(regionName=region)
    if cityRegion1.exists():
        print("region exit")
    else:
        print("region not exit, create")
        print(region)
        cityRegion1 = regionModels.objects.create(regionName=region)
    
    #print(regionModels.objects.get(regionName = region))


    #start to create city object
    cityObject = cityModels(
        cityName = name,
        cityRegion = regionModels.objects.get(regionName = region),
        cityTrueId = cityId
        )
    cityObject.save()
    print("finish create city")
    return cityObject

#输入地址名，可以返回有关这个地址的json
def gecodingAddress(address):
    datatype = "json"
    googeAPI = f"https://maps.googleapis.com/maps/api/geocode/{datatype}"
    key = "AIzaSyDzgKg6zPvAkeEVugOuHFJf7VNRx5VvZW4"
    address = address
    params = {"address": address,
              "language": 'en',
              "key": key
              }
    url_params = urlencode(params)
    url = f"{googeAPI}?{url_params}"
    with urllib.request.urlopen(url) as url:
        s = url.read()
        # I'm guessing this would output the html source code ?
        # print(s)
        s1 = str(s, 'utf-8')
        addressJson = json.loads(s1)
    return addressJson


#输入地址id，可以返回有关这个地址的所有详情
def placeJson(id):
    datatype = "json"
    googeAPI = f"https://maps.googleapis.com/maps/api/place/details/{datatype}"
    key = "AIzaSyDzgKg6zPvAkeEVugOuHFJf7VNRx5VvZW4"
    field ="type%2Cname%2COpening_Hours"
    params = {"place_id": id,
              "language": 'en',
              "field": field,
              "key":key
              }
    url_params = urlencode(params)
    url = f"{googeAPI}?{url_params}"
    with urllib.request.urlopen(url) as url:
        s = url.read()
        # I'm guessing this would output the html source code ?
        # print(s)
        s1 = str(s, 'utf-8')
        placeJson = json.loads(s1)
    return placeJson

#https://maps.googleapis.com/maps/api/place/details/json?language=en&field=type%2Cname%2COpening_Hours&place_id=ChIJs2n0CtJFiEgRg0leZQti8KM&key=AIzaSyDzgKg6zPvAkeEVugOuHFJf7VNRx5VvZW4

def searchSomethingInAddress(test,typeName):
    ln = ""
    for i in test:
        addressType = i.get("types")
        type1 = addressType[0]

        str2 = typeName
        # print(type(str2))
        # print(type(type1))

        if type1 == str2:
            ln = i.get("long_name")
            # print("0000000000")
            # print(ln)
    return ln