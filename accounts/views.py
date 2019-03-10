from django.shortcuts import render, redirect
from django.contrib import messages, auth

def login(request):
  if request.method == 'POST':
    # Login User
    username = request.POST['username']
    password = request.POST['password']

    user = auth.authenticate(username=username, password=password)
    if user is not None:
      auth.login(request,user)
      messages.success(request, 'You are now logged in')
      return redirect('dashboard')
    else:
      messages.error(request, 'Invalid credentials')
      return redirect('login')
  else:
    return render(request, 'accounts/login.html')

def logout(request):
  if request.method == 'POST':
    # Logout User
    auth.logout(request)
    messages.success(request, 'You are now logged out')
    return redirect('index')

def dashboard(request):
  return render(request, 'accounts/dashboard.html')

