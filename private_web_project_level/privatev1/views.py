from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def private_v1_1(request):
    return HttpResponse("private_v1_1")

def private_v1_2(request):
    return HttpResponse("private_v1_2")