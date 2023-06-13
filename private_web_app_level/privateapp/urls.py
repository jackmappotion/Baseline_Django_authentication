from django.urls import path
from .views import private_1, private_2

urlpatterns = [
    path("private_1", private_1),
    path("private_2", private_2),
]
