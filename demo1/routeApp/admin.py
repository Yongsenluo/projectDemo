from atexit import register
import imp
from django.contrib import admin
from .models import bigRouteModels,dayRouteModels,likeModels,commentModels

# Register your models here.

@admin.register(bigRouteModels)
class bigRouteAdmin(admin.ModelAdmin):
    pass

@admin.register(dayRouteModels)
class dayRouteAdmin(admin.ModelAdmin):
    pass

@admin.register(likeModels)
class likeAdmin(admin.ModelAdmin):
    pass

@admin.register(commentModels)
class commentAdmin(admin.ModelAdmin):
    pass