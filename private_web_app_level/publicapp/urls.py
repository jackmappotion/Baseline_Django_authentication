from django.urls import path
from .views import public_1, public_2

urlpatterns = [
    path("public_1", public_1),
    path("public_2", public_2),
]
