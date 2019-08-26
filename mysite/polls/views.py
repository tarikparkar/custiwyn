from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
import requests
#from .model import Stock
#from .serializers import StockSerializer

# Create your views here.
def index(request):
    response = requests.get('https://samples.openweathermap.org/data/2.5/weather?q=London,uk&appid=b6907d289e10d714a6e88b30761fae22')
    geodata = response.json()
    return render (request, 'home.html', {
        'ip' : geodata['ip'],
        'country' : geodata['country_name']
    })
