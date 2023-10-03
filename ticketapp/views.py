# from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.


def hello_world2(request):
    return HttpResponse("Hello, World2!")
