from django.shortcuts import render
import requests
from django.contrib.auth.decorators import login_required
from django.views.decorators.http import require_POST,require_GET

# Create your views here.

@login_required
@require_POST
def createRoute(requests):
    if requests.method == 'POST':
        # 大的行程路径生成了
        bigRouteForm = bigRouteForm(requests.POST)
        if bigRouteForm.is_valid():
            bigRouteObject =  bigRouteForm.save()
            
            #生成小的行程路径
            dayRouteForm = dayRouteForm(requests.POST)
            dayRouteForm.save()

            #每一个小行程路径里面的城市和景点要判断是否已经存在于数据库

        
        return render
    return render(requests,'createRoute.html')