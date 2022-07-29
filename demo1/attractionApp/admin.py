from django.contrib import admin

# Register your models here.
from .models import regionModels, categoryModels, cityModels, attractionModels
# Register your models here.


@admin.register(regionModels)
class regionAdmin(admin.ModelAdmin):
    pass
    #list_display = ('regionId', 'regionName', 'regionLikes')


@admin.register(cityModels)
class cityAdmin(admin.ModelAdmin):
    list_display = ('cityId', 'cityName', 'cityLikes', 'cityRegion')


@admin.register(categoryModels)
class categoryAdmin(admin.ModelAdmin):
    list_display = ('categoryId', 'categoryName', 'categoryLikes')


@admin.register(attractionModels)
class attractionAdmin(admin.ModelAdmin):
    list_display = ('attractionId', 'attractionName', 'attractionLat',
                    'attractionLng', 'attractionContent', 'attractionPostcode', 'attractionImg', 'attractionLikes', 'attractionCategory', 'attractionCity')
