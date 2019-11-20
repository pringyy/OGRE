
from django.http import HttpResponse
from django.shortcuts import render

def base(request):
	context_dict={}
	return render(request, 'points/base.html', context_dict)

def user_login(request):
	return render(request, 'points/login.html',{'login_message': 'Please enter your username and password'})