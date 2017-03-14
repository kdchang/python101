from django.shortcuts import render, redirect
from recipe.models import Recipe
from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from django.contrib import auth
from django.contrib import messages 
# Create your views here.

def get_index(request):
	recipes = Recipe.objects.all()
	for recipe in recipes:
		print(recipe.title)
	return render(request, 'index.html', locals())

def get_signup(request):
	return render(request, 'signup.html')

def post_signup(request):
	try:
		username = request.POST['username']
		email = request.POST['email']
		password = request.POST['password']
		print(username, email, password)
		user = User.objects.create_user(username, email, password)
		if user:
			return redirect('/', locals())
		else:
			messages.add_message(request, messages.SUCCESS, '註冊成功')
			return redirect('/signup', locals())
	except:		
		return redirect('/signup', locals())

def post_login(request):
	username = request.POST['username']
	password = request.POST['password']
	user = authenticate(username=username, password=password)
	print(user)
	if user is not None:
		auth.login(request, user)
		messages.add_message(request, messages.SUCCESS, '登入成功')
		return redirect('/', locals())
	
	messages.add_message(request, messages.SUCCESS, '請確認帳號密碼是否正確')
	return redirect('/', locals())	

def post_logout(request):
	auth.logout(request)
	messages.add_message(request, messages.SUCCESS, '登出成功')
	return redirect('/', locals())