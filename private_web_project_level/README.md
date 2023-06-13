# Django private_web project_level

```
superuser
    - id : admin
    - pw : 1234

app level authentication
    - privatev1
    - privatev2
```

## Using middleware
```
middleware.py

from django.shortcuts import redirect


class ProjectAccessMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        if not request.path.startswith('/admin/login') and not request.user.is_superuser:
            return redirect("/admin/login")
        return self.get_response(request)
------------------------------------------------------------------------------------------
settings.py
MIDDLEWARE = [
    .
    .
    .
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "private_web_project_level.middleware.ProjectAccessMiddleware",
]
```