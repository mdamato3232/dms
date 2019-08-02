from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib import messages, auth

def index(request):
  if request.user.is_authenticated:
    return render(request, 'pages/index.html')
  else:
    return redirect('login')

def planning(request):
  return render(request, 'pages/planning.html')

def collection(request):
  return render(request, 'pages/collection.html')

def dissemination(request):
  return render(request, 'pages/dissemination.html')



