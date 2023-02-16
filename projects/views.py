from django.shortcuts import render, redirect
from django.http import HttpResponse
# Create your views here.

def projects(request):
    return render(request, 'projects.html')

def project(request, pk):
    return render(request, 'single-project.html')
