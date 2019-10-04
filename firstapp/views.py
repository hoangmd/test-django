from django.shortcuts import render
import threading
import time
import requests
# Create your views here.
from django.http import HttpResponse

import os
from django.conf import settings


def index(request):
	file_ = open(os.path.join(settings.BASE_DIR, 'a.txt'))
	with open(file_, 'r') as f:
		s = f.readline()
	return HttpResponse('Hello, World!' + s)


   
