
from decimal import Decimal
import http
from urllib import request
from urllib.parse import urlencode
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import redirect

# Create your views here. 
from django.http import HttpResponse
from django.shortcuts import render
from django.conf import settings
import requests
from django.http import JsonResponse
import urllib, json
import urllib.request

# Create your views here.

# index method
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

def home(request):
	return render(request, 'home.html')

@csrf_exempt
def map(requests):
	if requests.method == 'POST':
		lat = requests.POST.get('lat')
		lng = requests.POST.get('lng')
		lat = Decimal(lat)
		lng = Decimal(lng)
		context =[lat,lng]
		return HttpResponse(lat)
	return render(requests,'map2.html')

@csrf_exempt
def geocoding(requests):
	if requests.method == 'POST':
		datatype = "json"
		googeAPI = f"https://maps.googleapis.com/maps/api/geocode/{datatype}"
		key = "AIzaSyDzgKg6zPvAkeEVugOuHFJf7VNRx5VvZW4"
		address = requests.POST.get('address')
		params = {"address":address,
					"key":key}
		url_params = urlencode(params)
		url = f"{googeAPI}?{url_params}"
		#----------------------
		with urllib.request.urlopen(url) as url:
			s = url.read()
			# I'm guessing this would output the html source code ?
			print(s)
			s1 = str(s,'utf-8')
			s1json = json.loads(s1)
			print(s1json)
			print('gaiogaio-------------->')
			print(s1json['results'][0].get(key))
			print('gaiogaio-------------->')
		#----------------------
		return HttpResponse(s1json)
	return render(requests,"testMap.html")