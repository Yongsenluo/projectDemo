from django.contrib import admin
from .models import UserInformation
# Register your models here.

@admin.register(UserInformation)
class userInformationAdmin(admin.ModelAdmin):
    list_display = ('userInformation_id','user','count_routes','count_likes','user_img')