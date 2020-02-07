from django.shortcuts import get_object_or_404, render
from django_tables2 import RequestConfig
from .models import Asset
from .tables import AssetTable
import pickle
from PIL import Image, ExifTags



def index(request):
  return render(request, 'assets/assets.html')

def asset(request, asset_id):
  asset = get_object_or_404(Asset, pk=asset_id)

  context = {
    'asset': asset
  }
  return render(request, 'assets/asset.html', context)

def search(request):
  queryset_list = Asset.objects.order_by('partnumber')

  # Keywords
  if 'keywords' in request.GET:
    keywords = request.GET['keywords']
    if keywords:
      queryset_list = queryset_list.filter(description__icontains=keywords)

  # Partnumber
  if 'partnumber' in request.GET:
    partnumber = request.GET['partnumber']
    if partnumber:
      queryset_list = queryset_list.filter(partnumber__icontains=partnumber)

  # Serialnumber
  if 'serialnumber' in request.GET:
    serialnumber = request.GET['serialnumber']
    if serialnumber:
      queryset_list = queryset_list.filter(serialnumber__icontains=serialnumber)

# Component. Since this is a foreign key, foreignkey__linked table__iexact.
  if 'component' in request.GET:
    component = request.GET['component']
    if component:
      queryset_list = queryset_list.filter(component__component__iexact=component)

# Sector. Since this is a foreign key, foreignkey__linked table__iexact.
  if 'sector' in request.GET:
    sector = request.GET['sector']
    if sector:
      queryset_list = queryset_list.filter(sector__sector__iexact=sector)

# Max Cost.
  if 'cost' in request.GET:
    cost = request.GET['cost']
    if cost:
      queryset_list = queryset_list.filter(cost__lt=cost)

  # Build the table for rendering
  table = AssetTable(queryset_list)

  grandtotal = 0
  for part in queryset_list:
    grandtotal += part.cost
  print("Grand total = " + str(grandtotal))

  RequestConfig(request).configure(table)

  context = {
    'grandtotal': grandtotal, 'table': table
  }
  return render(request, 'assets/search.html', context)
  
  
  
  
  if request.method == "POST":
  #   print("it's a get"  + request.method)
  #   # just present the form
  #   return render(request, 'assets/assets.html')
  # else:
    # read the form, do the query and filtering, render table.
    print("it's a post" + request.method)
    parts = Asset.objects.all()
    table = AssetTable(parts)
    print(table)
    print(parts)

    grandtotal = 0
    for part in parts:
      grandtotal += part.cost
    print("Grand total = " + str(grandtotal))

  if table:
    RequestConfig(request).configure(table)

    context = {'grandtotal': grandtotal, 'table': table}
  return render(request, 'assets/assets.html', context)

def rotate_image(filepath):
  try:
    image = Image.open(filepath)
    for orientation in ExifTags.TAGS.keys():
      if ExifTags.TAGS[orientation] == 'Orientation':
            break
    exif = dict(image._getexif().items())

    if exif[orientation] == 3:
        image = image.rotate(180, expand=True)
    elif exif[orientation] == 6:
        image = image.rotate(270, expand=True)
    elif exif[orientation] == 8:
        image = image.rotate(90, expand=True)
    image.save(filepath)
    image.close()
  except (AttributeError, KeyError, IndexError):
    # cases: image don't have getexif
    pass
