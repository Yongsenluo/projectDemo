from dataclasses import field
from tkinter import Widget
from django import forms

from demo1.attractionApp.models import attractionModels, cityModels
from . import models


class bigRouteForm(forms.ModelForm):
    class Metal:
        model = models.bigRouteModels
        fields = ["routeName", "routeUser", "routeImg"]


class dayRouteForm(forms.ModelForm):
    class Metal:
        model = models.dayRouteModels
        fields = ["dayRouteUser", "dayRoutetoBigRoute", "routeImg","dayRouteCity","dayRouteAttraction"]


        # 关于城市和景点，如果数据库里面没有人们想去的地方，他们可以通过谷歌地图添加
        #每天行程路径，建议人们只选择一个城市，一天不可能去两个城市
        # dayRouteCity = forms.ModelMultipleChoiceField(
        #     queryset=cityModels.objects.all(),
        #     widget=forms.CheckboxSelectMultiple
        # )
        

        dayRouteAttraction = forms.ModelMultipleChoiceField(
            queryset= attractionModels.objects.all(),
            widget = forms.CheckboxSelectMultiple
        )
