
from django.http import HttpResponse
from django.shortcuts import render

def base(request):
	context_dict={}
	return render(request, 'points/login.html', context_dict)

def user_login(request):
	return render(request, 'points/base.html',{'login_message': 'Please enter your username and password'})

def ogre_points(request):
	context_dict = {}

	return render(request, 'points/ogre_points.html', context_dict)