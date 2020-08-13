from django.shortcuts import render
from .models import *


PERSONAL = PersonalInfo.objects.first()

def home(request):
    context = {
        'personal': PERSONAL,
        'jobs': Job.objects.all().order_by('-id'),
    }
    return render(request,'portfolio/home.html', context)

def about(request):
    context = {
        'personal': PERSONAL,
        'title': 'About',
    }
    return render(request,'portfolio/about.html', context)

def projects(request):
    context = {
        'personal': PERSONAL,
        'projects': reversed(Project.objects.all().order_by('-id')),
        'title': 'Portfolio',
    }
    return render(request,'portfolio/projects.html', context)
