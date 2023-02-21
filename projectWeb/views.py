from django.shortcuts import render
from django.http import HttpResponse #Django library for HTTP 

def home(request):     #a view for the route of homepage
    return render(request, 'projectWeb/home.html', {})
