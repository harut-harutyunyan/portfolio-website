from django.shortcuts import render
from .models import *
from django.http import HttpResponse

def home(request):
    context = {
        'jobs': reversed(Job.objects.all()),
    }
    return render(request,'portfolio/home.html', context)

def about(request):
    context = {
        'title': 'About',
        'profile_pic': True,
    }
    return render(request,'portfolio/about.html', context)

def projects(request):
    context = {
        'projects': Project.objects.all(),
        'title': 'Portfolio',
    }
    return render(request,'portfolio/projects.html', context)
