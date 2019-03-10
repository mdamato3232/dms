from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib import messages, auth

def index(request):
  if request.user.is_authenticated:
    return render(request, 'pages/index.html')
  else:
    return redirect('login')

def about(request):
  return render(request, 'pages/about.html')



