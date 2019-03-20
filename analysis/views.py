from django.shortcuts import render
from processing.models import MissionData, Transmissions
from django_tables2 import RequestConfig
from .tables import MissionDataTable

def analysis(request):
  return render(request, 'analysis/analysis.html')

def viewmissions(request):
  queryset_list = MissionData.objects.order_by('-uploaded_at')
  table = MissionDataTable(queryset_list)

  RequestConfig(request).configure(table)

  context = {
    'table': table
  }
  return render(request, 'analysis/missiondata.html', context)

  

