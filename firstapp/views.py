from django.shortcuts import render
import threading
import time
import requests
# Create your views here.
from django.http import HttpResponse

def index(request):
	r = requests.get(r'https://www.youtube.com/results?search_query=two+steps+from+hell+victory').text
	return HttpResponse('Hello, World!' + str(r))


   
