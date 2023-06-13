# Django private_web view_level

```
superuser
    - id : admin
    - pw : 1234

view level authentication
    - private_1 : only superuser
    - private_2 : only superuser
    
    - public_1 : all
    - public_2 : all
```

## views.py
```
from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.decorators import user_passes_test

# Create your views here.

@user_passes_test(lambda user : user.is_superuser, login_url='/admin/login')
def private_1(response):
    return HttpResponse("private_1")
-> user_passes_test 이후 만약 유저가 슈퍼유저 아니면 localhost:8000/admin/login (슈퍼유저 로그인 session으로 넘어감)

@user_passes_test(lambda user : user.is_superuser, login_url='/admin/login')
def private_2(response):
    return HttpResponse("private_2")
-> user_passes_test 이후 만약 유저가 슈퍼유저 아니면 localhost:8000/admin/login (슈퍼유저 로그인 session으로 넘어감)

def public_1(response):
    return HttpResponse("public_1")

def public_2(response):
    return HttpResponse("public_2")

```