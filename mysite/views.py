from django.shortcuts import render
from django.http import HttpResponse

def index(request):
	myname = "球球"
	return render(request,'index.html',locals())
