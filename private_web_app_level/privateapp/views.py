from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def private_1(response):
    return HttpResponse("private_1")


def private_2(response):
    return HttpResponse("private_2")
