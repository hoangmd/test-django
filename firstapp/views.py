from django.shortcuts import render
import threading
import time
import requests
# Create your views here.
from django.http import HttpResponse

import os
from django.conf import settings


def index(request):
	with open(os.path.join(settings.BASE_DIR, 'a.txt'), 'r') as f:
		s = f.readline()
	return HttpResponse('Hello, World!' + s)


   
