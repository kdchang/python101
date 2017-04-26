from django.shortcuts import render, redirect
from recipe.models import Recipe
from datetime import datetime, timedelta

from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from django.contrib import auth


# Create your views here.

def get_index(request):
	title = 'OpenCook'
	recipes = Recipe.objects.all()
	response = render(request, 'index.html', locals())
	return response

def get_signup(request):
	return render(request, 'signup.html')

def post_signup(request):
	username = request.POST['username']
	email = request.POST['email']
	password = request.POST['password']

	user = User.objects.create_user(username, email, password)
	if user:
		return redirect('/', locals())
	else:
		redirect('/signup', locals())
	
def post_logout(request):
	auth.logout(request)
	return redirect('/')

def get_shop(request):
	return render(request, 'shop.html')

def post_login(request):
	username = request.POST['username']
	password = request.POST['password']

	user = authenticate(username=username, password=password)

	if user is not None:
		auth.login(request, user)
		return redirect('/', locals())
	else:
		return redirect('/', locals())
		