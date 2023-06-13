from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.decorators import user_passes_test

# Create your views here.

@user_passes_test(lambda user : user.is_superuser, login_url='/admin/login')
def private_1(response):
    return HttpResponse("private_1")

@user_passes_test(lambda user : user.is_superuser, login_url='/admin/login')
def private_2(response):
    return HttpResponse("private_2")

def public_1(response):
    return HttpResponse("public_1")

def public_2(response):
    return HttpResponse("public_2")
