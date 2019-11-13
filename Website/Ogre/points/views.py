
from django.http import HttpResponse
from django.shortcuts import render

def index(request):
	context_dict = {'boldmessage: Hello'}
	return render(request, 'points/home.html', context = context_dict)