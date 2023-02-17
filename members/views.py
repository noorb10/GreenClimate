from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.forms import UserCreationForm
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required 
from django.contrib.auth.models import Group 

from .forms import CreateUserForm
from .decorators import unauthenticated_user, allowed_users
from django.contrib import messages

@unauthenticated_user
def signup_user(request):
	form = CreateUserForm()
	if request.method == "POST":
		form = CreateUserForm(request.POST)
		if form.is_valid():
			user = form.save()
			username = form.cleaned_data['username']
			password = form.cleaned_data['password1']

			user = authenticate(username=username, password=password)
			login(request, user)

			group = Group.objects.get(name='client') #every new account is set to client group
			user.groups.add(group)
			user_msg = form.cleaned_data.get('username')
			messages.success(request, "Registration Successful! Account was created for " + user_msg + ".")
			return redirect('home')
	else:
		form = CreateUserForm()
	return render(request, 'authenticate/signup.html', {'form':form, })

@unauthenticated_user
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

@login_required(login_url='login') #Restricts access, unless authenticated! 
@allowed_users(allowed_roles=['client']) #Allows access based on groups.
def user_page(request):
	return render(request, 'authenticate/user.html', {})

@login_required(login_url='login') #Restrict access, unless authenticated! 
def community(request):
	return render(request, 'authenticate/community.html', {})

@login_required(login_url='login') #Restrict access, unless authenticated! 
def settings(request):
	return render(request, 'authenticate/settings.html', {})