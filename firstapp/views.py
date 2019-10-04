from django.shortcuts import render
import threading
import time
import requests
# Create your views here.
from django.http import HttpResponse


running = False
def start(request):
	a = 0
	#r = requests.get(r'https://www.youtube.com/results?search_query=two+steps+from+hell+victory').text
	while True:
		a += 1
		request.session['a'] = str(a)
 
def index(request, run):
	request.session['a'] = '0'
	if run == 1:
		t = threading.Thread(target=start, args=(request,))
		t.start()
	return HttpResponse('Hello, World!' + request.session['a'])


   
