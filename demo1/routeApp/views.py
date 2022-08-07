import imp
import json
from django.http import HttpResponse
from django.shortcuts import render
from numpy import tile
import requests
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User


from attractionApp.models import categoryModels, regionModels
from django.views.decorators.csrf import csrf_exempt

from routeApp.models import bigRouteModels, dayRouteModels, recommendModels
# Create your views here.


@login_required
@csrf_exempt
# @require_POST
def createRoute(requests):
    # if requests.method == 'POST':
    #     # 大的行程路径生成了
    #     bigRouteForm = bigRouteForm(requests.POST)
    #     if bigRouteForm.is_valid():
    #         bigRouteObject =  bigRouteForm.save()

    #         #生成小的行程路径
    #         dayRouteForm = dayRouteForm(requests.POST)
    #         dayRouteForm.save()

    #         #每一个小行程路径里面的城市和景点要判断是否已经存在于数据库

    #     return HttpResponse("hi")

    # 先获取region和category的所有元素
    cityRegion = regionModels.objects.all()
    attractionCategory = categoryModels.objects.all()
    # print(cityRegion)

    if requests.method == 'POST':
        # print(requests.POST)
        # post_data =  requests.POST.get('post_data',None)
        # print('----->post_data:',post_data)

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
            routeDay = days
        )
        bigRouteObject.save()

        # 开始创建 day route 对象,根据days的多少创建多少，city 和attractions 都是后来再添加
        for i in range(1, days+1, +1):
            #print(i)
            dayRouteObject = dayRouteModels(
                dayRouteUser=user,
                dayRoutetoBigRoute=bigRouteObject,
                dayRouteNumber=i,
            )
            print(dayRouteObject)
            dayRouteObject.save()

        #创建recommend 对象
        recommendObject = recommendModels(
            recommendBigRoute = bigRouteObject
        )
        recommendObject.save()

        #创建M2M的recommend 和region 关系
        for h in citys_Id:
            #print(h)
            region = regionModels.objects.get(regionId = h)
            print("----------------------->>")
            print(region)
            # m2mRectoRegionObject = M2MRecommendtoRegion(
            #     recommend=recommendObject,
            #     region = region
            # )
            # print(m2mRectoRegionObject.region)
            # m2mRectoRegionObject.save()
            recommendObject.recommendRegion.add(region)
        
        #创建M2M的recommend 和 Category关系
        for g in categorys_Id:
            #print(g)
            category = categoryModels.objects.get(categoryId = g)
            print("----------------------->>")
            print(category)
            # m2mRectoCateObject = M2MRecommendtoCategory(
            #     recommend=recommendObject,
            #     category = category
            # )
            # print(m2mRectoCateObject.category)
            # m2mRectoCateObject.save()
            recommendObject.recommendCategory.add(category)
        print(recommendObject.recommendCategory.all())
        print(recommendObject.recommendRegion.all())

    context = {
        'region': cityRegion,
        'category': attractionCategory
    }

    return render(requests, 'createRoute.html', context=context)
