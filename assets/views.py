from django.shortcuts import render
from django_tables2 import RequestConfig
from .models import Asset
from .tables import AssetTable



def index(request):
  table = AssetTable(Asset.objects.all())
  RequestConfig(request).configure(table)
  return render(request, 'assets/assets.html', {'table': table})

def asset(request):
  return render(request, 'assets/asset.html')

def search(request):
  return render(request, 'assets/search.html')
