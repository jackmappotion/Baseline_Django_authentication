from django.shortcuts import redirect

class SuperuserMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        if request.path.startswith('/private/') and not request.user.is_superuser:
            return redirect("/admin/login")
        return self.get_response(request)
