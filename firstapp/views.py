from django.shortcuts import render
import threading
import time
import requests
# Create your views here.
from django.http import HttpResponse


running = False
a = 0
def run():
	#r = requests.get(r'https://www.youtube.com/results?search_query=two+steps+from+hell+victory').text
	while True:
		a += 1
 
def index(request):
	if not running:
		running = True
		t = threading.Thread(target=run)
		t.start()
	return HttpResponse('Hello, World!' + str(a))


   
