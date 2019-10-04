from django.shortcuts import render
import threading
import time
import requests
# Create your views here.
from django.http import HttpResponse


running = False
a = 0
def start():
	#r = requests.get(r'https://www.youtube.com/results?search_query=two+steps+from+hell+victory').text
	while True:
		a += 1
 
def index(request, run):
	if run == 1:
		t = threading.Thread(target=start)
		t.start()
	return HttpResponse('Hello, World!' + str(a))


   
