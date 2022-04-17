
from multiprocessing import context
from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.forms import inlineformset_factory
from django.contrib.auth.forms import UserCreationForm
from .models import *
from .forms import  CreateUserForm
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .decorators import unauthenticated_user, allowed_users, admin_only


@unauthenticated_user
def  register_request(request):  #if the user is already logged in move him to home page
		form = CreateUserForm()
		if request.method == 'POST':
			form = CreateUserForm(request.POST)
			if form.is_valid():
				user = form.save()
				username = form.cleaned_data.get('username')
				messages.success(request, 'Account was created for ' + username)

				return redirect('login')

		context = {'form':form}
		return render(request, 'html/register.html', context)

	
def home(request):       
    return render(request, 'html/home.html')


def contact(request):   
    return render(request, 'html/contactus.html')


def rule(request): 
    return render(request, 'html/rule.html')

def forum(request): 
    return render(request, 'html/forum.html')

def about(request): 
    return render(request, 'html/about.html')

@unauthenticated_user
def loginPage(request):
	if request.method == 'POST':         #match username and password from th existing database
			username = request.POST.get('username')
			password = request.POST.get('password')

			user = authenticate(request, username=username, password=password)

			if user is not None:
				login(request, user)
				return redirect('home')
			else:
				messages.info(request, 'Username OR password is incorrect')

	context = {}
	return render(request, 'html/login.html', context)

def logoutUser(request):    #logout the customer and redirect to login page
	logout(request)
	return redirect('login')

@login_required(login_url='login')  # before displayong home page show login then go further
@admin_only
def home(request):
	customers=customer.objects.all()
	context={'customers': customers}
	return render(request, 'html/home.html',context)