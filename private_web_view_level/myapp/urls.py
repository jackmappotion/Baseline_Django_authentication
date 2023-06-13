from django.urls import path
from .views import private_1, private_2
from .views import public_1, public_2

urlpatterns = [
    path("private_1/", private_1),
    path("private_2/", private_2),
    
    path("public_1/", public_1),
    path("public_2/", public_2),
]
