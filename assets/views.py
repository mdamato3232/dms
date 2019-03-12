from django.shortcuts import get_object_or_404, render
from django_tables2 import RequestConfig
from .models import Asset
from .tables import AssetTable



def index(request):
  if request.method == "GET":
    print("it's a get"  + request.method)
    # just present the form
    return render(request, 'assets/assets.html')
  else:
    # read the form, do the query and filtering, render table.
    print("it's a post" + request.method)
    table = AssetTable(Asset.objects.all())
    RequestConfig(request).configure(table)
    return render(request, 'assets/assets.html', {'table': table})

def asset(request, asset_id):
  asset = get_object_or_404(Asset, pk=asset_id)

  context = {
    'asset': asset
  }
  return render(request, 'assets/asset.html', context)

def search(request):
  return render(request, 'assets/search.html')
