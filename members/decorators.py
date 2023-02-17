from django.http import HttpResponse
from django.shortcuts import redirect


def unauthenticated_user(view_func):
    def wrapper_func(request, *args, **kwargs):
        if request.user.is_authenticated:
            return redirect('home') #if user is authenticated redirect to home.
        else:
            return view_func(request, *args, **kwargs)
    return wrapper_func #if user isn't authenticated redirect to login or register page.

def allowed_users(allowed_roles=[]):
    def decorator(view_func):
        def wrapper_func(request, *args, **kwargs):
            
            group = None
            if request.user.groups.exists():
                group = request.user.groups.all()[0].name

            if group in allowed_roles:
                return view_func(request, *args, **kwargs)
            else:
                html = "<h1> You are not authorized to view this page!</h1> <br> <button type=\"button\" name=\"home\"><a href=\"/home.html\">Back to the Home Page</a></button>"
                response = HttpResponse(html, content_type="text/html")
                return(response)
                
        return wrapper_func
    return decorator