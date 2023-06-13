# Django private_web app_level

```
superuser
    - id : admin
    - pw : 1234

app level authentication
    - privateapp
    - publicapp
```

## Using middleware
```
middleware.py

from django.shortcuts import redirect

class SuperuserMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        if request.path.startswith('/private/') and not request.user.is_superuser:
            return redirect("/admin/login")
        return self.get_response(request)
------------------------------------------------------------------------------------------
settings.py
MIDDLEWARE = [
    .
    .
    .
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "private_web_app_level.middleware.SuperuserMiddleware",
]
```