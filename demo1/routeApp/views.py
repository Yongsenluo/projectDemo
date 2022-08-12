import imp
import json
from telnetlib import AO, RCP
from unittest import result
from django.http import HttpResponse, JsonResponse
from django.shortcuts import redirect, render
from numpy import tile
import requests
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User


from attractionApp.models import attractionModels, categoryModels, cityModels, regionModels
from django.views.decorators.csrf import csrf_exempt

from routeApp.models import bigRouteModels, dayRouteModels, recommendModels
from django.urls import reverse
# Create your views here.


@login_required
@csrf_exempt
# @require_POST
def createRoute(requests):
    cityRegion = regionModels.objects.all()
    attractionCategory = categoryModels.objects.all()
    # print(cityRegion)

    if requests.method == 'POST':
        post_data = json.loads(requests.body)
        print(post_data)
        user_id = post_data.get('user')
        title = post_data.get('title')
        days = int(post_data.get('days'))
        citys_Id = post_data.get('city')
        categorys_Id = post_data.get('category')

        user = User.objects.get(id=user_id)
        # 开始创建big route 对象
        bigRouteObject = bigRouteModels(
            routeName=title,
            routeUser=user,
            routeDay=days
        )
        bigRouteObject.save()

        # 开始创建 day route 对象,根据days的多少创建多少，city 和attractions 都是后来再添加
        for i in range(1, days+1, +1):
            # print(i)
            dayRouteObject = dayRouteModels(
                dayRouteUser=user,
                dayRoutetoBigRoute=bigRouteObject,
                dayRouteNumber=i,
            )
            print(dayRouteObject)
            dayRouteObject.save()

        # 创建recommend 对象
        recommendObject = recommendModels(
            recommendBigRoute=bigRouteObject
        )
        recommendObject.save()

        # 创建M2M的recommend 和region 关系
        for h in citys_Id:
            # print(h)
            region = regionModels.objects.get(regionId=h)
            print("----------------------->>")
            print(region)
            # m2mRectoRegionObject = M2MRecommendtoRegion(
            #     recommend=recommendObject,
            #     region = region
            # )
            # print(m2mRectoRegionObject.region)
            # m2mRectoRegionObject.save()
            recommendObject.recommendRegion.add(region)

        # 创建M2M的recommend 和 Category关系
        for g in categorys_Id:
            # print(g)
            category = categoryModels.objects.get(categoryId=g)
            print("----------------------->>")
            print(category)

            recommendObject.recommendCategory.add(category)
        print(recommendObject.recommendCategory.all())
        print(recommendObject.recommendRegion.all())
        bigRoute_id = bigRouteObject.routeId
        url = '/createDayRoute/id=' + str(bigRoute_id)
        return JsonResponse({'msg': url})

    context = {
        'region': cityRegion,
        'category': attractionCategory
    }

    return render(requests, 'createRoute.html', context=context)


@csrf_exempt
def createDayRoute(requests, bigRoute_id):
    bigRouteObject = bigRouteModels.objects.get(routeId=bigRoute_id)
    print(bigRouteObject)
    allDayRouteObjecs = dayRouteModels.objects.filter(
        dayRoutetoBigRoute=bigRouteObject).order_by('dayRouteNumber')

    # if requests.method == 'POST':
    #     dayRoute_id = int(requests.POST.get('dayRouteId'))
    #     dayRouteObject = dayRouteModels.objects.get(dayRouteId = dayRoute_id)
    #     print(dayRouteObject)
    #     return JsonResponse({'dayobject':dayRouteObject})

    return render(requests, 'createDayRoute.html', {'bigRouteObject': bigRouteObject, 'allDayRouteObjecs': allDayRouteObjecs})


def addAttration(requests, bigRouteObject,dayRouteObject):
    try:
        print(dayRouteObject)
        br = bigRouteObject
        ro = recommendModels.objects.get(recommendBigRoute=br)
        #所有推荐的景点种类对象
        rc = ro.recommendCategory.all()
        print(rc)

        #所有推荐的region对象
        rr = ro.recommendRegion.all()
        print(rr)

        #找到所有region=推荐的city
        for i in rr:
            allCity = cityModels.objects.filter(cityRegion = i)
        # print("...................")
        #print(allCity)


        dayRouteCityObject2 = dayRouteObject.dayRouteCity.all()
        allAttractionResult={}
        #！！！！！！！！！！！！！！！！！！！！！！！！！！！ bug
        #这里还是有问题，当category>1 的时候，for i in rc 遍历走不下去，alltractionResult不包含第二次遍历的结果
        #找到所有category=推荐的attracation
        for i in rc:
            attraction = attractionModels.objects.filter(attractionCategory = i).order_by('-attractionLikes')
            #print(attraction)
            for h in dayRouteCityObject2:
                #print(h.cityName)
                result = attraction.filter(attractionCity = h)
                if result.exists():
                    allAttractionResult=result
        print("...................qqqqqq")
        print(allAttractionResult)
        todayCity = dayRouteObject.dayRouteCity.all()
        if todayCity.count() ==0:
            str = "You haven't picked a city yet"
            todayCity = str


        # print("...........teste!!!!")
        # print(todayCity)

        #首先找到城市为todayCity的景点

        #除了推荐的，还有其他在这个城市著名的景点

        dayRouteCityObject = dayRouteObject.dayRouteCity.all()
        #空的原因是，前端还没有选去的城市
        print(dayRouteCityObject)
        for j in dayRouteCityObject:
            aObject = attractionModels.objects.filter(attractionCity=j).order_by('-attractionLikes')
            if aObject.count() == 0:
                break
            else:
                print("giaogiaogiao")
                print(aObject)
                for h in allAttractionResult:
                    #print(h)
                    aObject = aObject.exclude(attractionId = h.attractionId)
                    #print("删除后。。。。")
                    #print(aObject)
                excludeRelist = aObject
        

        print(excludeRelist)
        # print('hihihihihi..............')
        # print(excludeReList)


        dir = {
            'dayRouteObject':dayRouteObject,
            'recommendCategory': rc,
            'recommendRegion': rr,
            'recommendCity':allCity,
            'allAttractionResult':allAttractionResult,
            'todayCity':todayCity,
            'excludeReList': excludeRelist,
        }
        return dir
    except:
        return HttpResponse("You didn't select the city")

@csrf_exempt
def addCityMethod(requests,bigRouteObject,dayRouteObject):
    br = bigRouteObject
    ro = recommendModels.objects.get(recommendBigRoute=br)

    #所有推荐的region对象
    rr = ro.recommendRegion.all()
    print(rr)

    #找到所有region=推荐的city
    for i in rr:
        allCity = cityModels.objects.filter(cityRegion = i)

    allCity = allCity.order_by("-cityLikes")
    #除了推荐的城市，把其他城市找出来
    cityObjectAll = cityModels.objects.all().order_by('-cityLikes')
    # cityObjectAll.exclude(allCity)
    print(".................")
    for j in allCity:
        cityObjectAll = cityObjectAll.exclude(cityId = j.cityId)

    
    print(cityObjectAll)

    dir = {
        'recommendRegion': rr,
        'recommendCity':allCity,
        'dayRouteObject':dayRouteObject,
        'otherCity':cityObjectAll,
    }

    return dir



@csrf_exempt
def everyDayMap(requests,dayRouteObject):
    attractionObjects =  dayRouteObject.dayRouteAttraction.all()
    print(attractionObjects)
    dir = []
    for i in attractionObjects:    
        latLng = {}
        lat = i.attractionLat
        lng = i.attractionLng
        latLng = {
            'lat':lat,
            'lng':lng
        }
        print(latLng)

        dir.append(latLng)
    
    print(dir)
        
    return attractionObjects


@csrf_exempt
def dayRouteDetail(requests, dayRoute_id):
    try:
        dayRouteObject = dayRouteModels.objects.get(dayRouteId=dayRoute_id)
        bigRouteObject = dayRouteObject.dayRoutetoBigRoute
        dayRouteCity = dayRouteObject.dayRouteCity.all()
        dayRouteAttraction = dayRouteObject.dayRouteAttraction.all()
        content = {
            'dayRouteObject': dayRouteObject,
            'dayRouteCity': dayRouteCity,
            'dayRouteAttraction': dayRouteAttraction,
        }
        # print("giao....")
        # print(dayRouteCity)

        if requests.method == 'POST':
            deleteButton = requests.POST.get('delete_button')
            deleteButtonCity = requests.POST.get('delete_button_city')
            addCity = requests.POST.get('addCity')
            addAttractionButton = requests.POST.get("addAttraction")
            mapButton = requests.POST.get("map")
            if deleteButton is not None:
                print("这里是delete")
                attractionId = int(requests.POST.get('delete_button'))
                attractionObject = attractionModels.objects.get(
                    attractionId=attractionId)
                print(dayRouteObject.dayRouteAttraction.all())
                print("删除后。。。。。。")
                dayRouteObject.dayRouteAttraction.remove(attractionObject)
                print(dayRouteObject.dayRouteAttraction.all())
                content = {
                    'dayRouteObject': dayRouteObject,
                    'dayRouteCity': dayRouteCity,
                    'dayRouteAttraction': dayRouteAttraction,
                }
                return render(requests, 'dayRouteTem.html', content)

            elif deleteButtonCity is not None:
                print("here is city delete")
                cityId = int(requests.POST.get('delete_button_city'))
                cityObject = cityModels.objects.get(cityId = cityId)
                dayRouteObject.dayRouteCity.remove(cityObject)
                content = {
                    'dayRouteObject': dayRouteObject,
                    'dayRouteCity': dayRouteCity,
                    'dayRouteAttraction': dayRouteAttraction,
                }
                return render(requests, 'dayRouteTem.html', content)
            elif addAttractionButton is not None:
                print("这里是add attraction")
                dir = addAttration(requests, bigRouteObject,dayRouteObject)
                return render(requests, 'addatt.html', dir)
            elif addCity is not None:
                print("这里是add city")
                dir = addCityMethod(requests,bigRouteObject,dayRouteObject)
                return render(requests, 'addCity.html',dir)
            elif mapButton is not None:
                dir = everyDayMap(requests,dayRouteObject=dayRouteObject)
                content={
                    'dir':dir,
                    'dayRouteObject':dayRouteObject
                }
                return render(requests, 'everyDayMap.html',content)
            else:
                return HttpResponse("什么都没有")

        return render(requests, 'dayRouteTem.html', content)
    except:
        return HttpResponse("please select the city")


@csrf_exempt
def addCity(requests):
    if requests.method == 'POST':
        post_data = json.loads(requests.body)
        #print(post_data)
        cityId =  post_data.get('city')
        dayRoute_Id =  post_data.get('dayRoute_Id')
        dayRouteObject = dayRouteModels.objects.get(dayRouteId = dayRoute_Id)
        for i in cityId:
            cityObject = cityModels.objects.get(cityId = i)
            # 把选中的city 加入到dayRoute中
            dayRouteObject.dayRouteCity.add(cityObject)
        print("添加成功")

    url = '/dayRouteTem/dayRouteId='+ dayRoute_Id
    return JsonResponse({'msg': url})


@csrf_exempt
def addAttraction2(requests):
    if requests.method == 'POST':
        post_data = json.loads(requests.body)
        #print(post_data)
        attractionId =  post_data.get('attraction')
        dayRoute_Id =  post_data.get('dayRoute_Id')
        dayRouteObject = dayRouteModels.objects.get(dayRouteId = dayRoute_Id)
        for i in attractionId:
            attractionObject = attractionModels.objects.get(attractionId = i)
            # 把选中的city 加入到dayRoute中
            dayRouteObject.dayRouteAttraction.add(attractionObject)
        print("添加成功")

    url = '/dayRouteTem/dayRouteId='+ dayRoute_Id
    return JsonResponse({'msg': url})


