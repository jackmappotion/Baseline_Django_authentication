from django.apps import AppConfig
from django.contrib.auth.decorators import user_passes_test

class PrivateappConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'privateapp'