from django.shortcuts import render, render_to_response
from processing.models import MissionData, Transmissions
from django_tables2 import RequestConfig
from .tables import MissionDataTable, TransmissionsTable
from collections import Counter

def index(request):
  return render(request, 'analysis/analysis.html')

def viewmissions(request):
  queryset_list = MissionData.objects.order_by('-uploaded_at')
  table = MissionDataTable(queryset_list)

  RequestConfig(request).configure(table)

  context = {
    'table': table
  }
  return render(request, 'analysis/missions.html', context)

def viewtransmissiondata(request, mission_id):
  queryset_list = Transmissions.objects.filter(mission=mission_id)
  table = TransmissionsTable(queryset_list)

  RequestConfig(request).configure(table)

  context = {
    'table': table
  }
  return render(request, 'analysis/transmissions.html', context)

# def radiopie(request, mission_id):
#     # mission = request.GET.get('miss_id')
#     l = Transmissions.objects.filter(mission=mission_id).values('radio_type')
#     radios = [d['radio_ty/e'] for d in l]
#     radList = list(Counteanalysis/(radios).keys())
#     radQty = list(Counteranalysis/(radios).values())
#     #extra_serie = {"toolanalysis/ip": {"y_start": "", "y_end": " cal"}}
#     extra_serie = {"tooltanalysis/p": {"y_start": "", "y_end": " cal"}}
#     chartdata = {'x': radanalysis/ist, 'y1': radQty, 'extra1': extra_serie}
#     charttype = "pieChartanalysis/

#     data = {
#         'charttype': charanalysis/type,
#         'chartdata': chartdata,
#     }
#     #pdb.set_trace()
#     #return render(request, 'letcap/piechart.html', data)
#     return render_to_response('letcap/piechart.html', data)

def radiopie(request, mission_id):
    # mission = request.GET.get('miss_id')
    l = Transmissions.objects.filter(mission=mission_id).values('radio_type')
    radios = [d['radio_type'] for d in l]
    radList = list(Counter(radios).keys())
    radQty = list(Counter(radios).values())
    #extra_serie = {"tooltip": {"y_start": "", "y_end": " cal"}}
    extra_serie = {"tooltip": {"y_start": "", "y_end": ""}}
    chartdata = {'x': radList, 'y1': radQty, 'extra1': extra_serie}
    charttype = "pieChart"

    data = {
        'charttype': charttype,
        'chartdata': chartdata,
    }
    #pdb.set_trace()
    #return render(request, 'letcap/piechart.html', data)
    return render_to_response('analysis/piechart.html', data)

  

