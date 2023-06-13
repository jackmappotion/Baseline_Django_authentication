from django.urls import path
from .views import private_v2_1, private_v2_2

urlpatterns = [
    path("private_1", private_v2_1),
    path("private_2", private_v2_2),
]
