

from multiprocessing import context
from django.shortcuts import render

# Create your views here. 
from django.http import HttpResponse
from django.shortcuts import render
from django.conf import settings
import requests
# Create your views here.

def index(request):

   
    
	context = {
	"google_api_key": settings.GOOGLE_API_KEY,
	"base_country": settings.BASE_COUNTRY}
    

	return render(request, 'index.html', context)


# def index(request):
#     url = 'https://maps.googleapis.com/maps/api/directions/outputFormat?parameters'

#     context = {
# 		#'up_form':up_form,
# 		'google_api_key': settings.GOOGLE_API_KEY
# 		}
	
    
#     return render(request,'index.html',context)
#     #return HttpResponse('dsadada')