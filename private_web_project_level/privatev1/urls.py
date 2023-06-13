from django.urls import path
from .views import private_v1_1, private_v1_2

urlpatterns = [
    path('private_1', private_v1_1),
    path('private_2', private_v1_2),
]
