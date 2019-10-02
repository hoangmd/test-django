from django.shortcuts import render
import threading
import time
# Create your views here.
from django.http import HttpResponse

def index(request):
	t = threading.Thread(target=worker)
	t.start()
	return HttpResponse('Hello, World!')


def worker():
	while True:
		time.sleep(1)
		with open("a.txt", 'a') as f:
			f.write("hello\n")
   
