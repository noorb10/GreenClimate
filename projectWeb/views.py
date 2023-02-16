from django.shortcuts import render
from django.http import HttpResponse #Django library for HTTP 

def home(request):     #a view for the route of homepage
    return render(request, 'projectWeb/home.html', {})

# def signup(request):
#     if request.method == "POST":
#         username = request.POST = ['username']
#         email = request.POST = ['email']
#         password = request.POST = ['password']
#         rePassword = request.POST = ['rePassword']
#         return render (request, 'projectWeb/signup.html', {'username': username})
#     else:
#         return render (request, 'projectWeb/signup.html', {})
