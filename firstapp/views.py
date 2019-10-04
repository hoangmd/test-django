from django.shortcuts import render
import threading
import time
import requests
# Create your views here.
from django.http import HttpResponse



def index(request):
	with open("a.txt", 'r') as f:
		s = f.readline()
	return HttpResponse('Hello, World!' + s)


   
