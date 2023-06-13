from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def public_1(response):
    return HttpResponse("public_1")

def public_2(response):
    return HttpResponse("public_2")