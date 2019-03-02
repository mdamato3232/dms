from django.shortcuts import render

def index(request):
  return render(request, 'assets/assets.html')

def asset(request):
  return render(request, 'assets/asset.html')

def search(request):
  return render(request, 'assets/search.html')
