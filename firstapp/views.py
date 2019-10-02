from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from background_task import background


def index(request):
    return HttpResponse('Hello, World!')


@background(schedule=5)
def hello():
	print "Hello World!"
