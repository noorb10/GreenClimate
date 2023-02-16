from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.forms import UserCreationForm
from django.http import HttpResponse

from .forms import CreateUserForm
from django.contrib import messages


def signup_user(request):
	form = CreateUserForm()
	if request.method == "POST":
		form = CreateUserForm(request.POST)
		if form.is_valid():
			form.save()
			username = form.cleaned_data['username']
			password = form.cleaned_data['password1']
			user = authenticate(username=username, password=password)
			login(request, user)
			user_msg = form.cleaned_data.get('username')
			messages.success(request, "Registration Successful! Account was created for " + user_msg + ".")
			return redirect('home')
	else:
		form = CreateUserForm()
	return render(request, 'authenticate/signup.html', {'form':form, })


def login_user(request):
	if request.method == "POST":
		username = request.POST['username']
		password = request.POST['password']
		user = authenticate(request, username=username, password=password)
		if user is not None:
			login(request, user)
			return redirect('home')
		else:
			messages.success(request, ("There was an error logging in! Check username and password."))	
			return redirect('login')	
	else:
		return render(request, 'authenticate/login.html', {})


def logout_user(request):
	logout(request)
	messages.success(request, ("You were logged out!"))
	return redirect('home')

def user_page(request):
	return render(request, 'authenticate/user.html', {})

def settings(request):
	return render(request, 'authenticate/settings.html', {})