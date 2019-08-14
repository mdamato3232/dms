from django.shortcuts import render, render_to_response
from processing.models import MissionData, Transmissions
from django_tables2 import RequestConfig
from .tables import MissionDataTable, TransmissionsTable
from collections import Counter
from .forms import QueryForm
from django.http import HttpResponse, HttpResponseRedirect


def index(request):
  return render(request, 'analysis/analysis.html')

def dbquery(request):
  # if this is a POST request we need to process the form data
  if request.method == 'POST':
    # create a form instance and populate it with data from the request:
    form = QueryForm(request.POST)
    # check whether it's valid:
    if form.is_valid():
        # process the data in form.cleaned_data as required
        StartFreq = form.cleaned_data['start_freq']
        print('Start Freq = %s' % StartFreq)
        StartFreq = int(StartFreq * 1000000)
        print('Start Freq mutliplied = %s' % StartFreq)

        # queryset_list = Transmissions.objects.filter(profile_frequency__gte = 451850000).filter(profile_frequency__lte = 461000000).filter(timestamp_local__gte='2019-07-16 23:51:47+00')
        queryset_list = Transmissions.objects.filter(profile_frequency = StartFreq)
        print('Number of records returned = %s' % len(queryset_list))
        table = TransmissionsTable(queryset_list)

        RequestConfig(request).configure(table)

        context = {
          'table': table
        }
        return render(request, 'analysis/transmissions.html', context)

        # # redirect to a new URL:
        # return HttpResponseRedirect('/analysis/')

  # if a GET (or any other method) we'll create a blank form
  else:
      form = QueryForm()

  return render(request, 'analysis/dbquery.html', {'form': form})





  # # queryset_list = Transmissions.objects.filter(profile_frequency__gte = 451850000).filter(profile_frequency__lte = 461000000).filter(timestamp_local__gte='2019-07-16 23:51:47+00')
  # queryset_list = Transmissions.objects.filter(profile_frequency = StartFreq)
  # print('Number of records returned = %s' % len(queryset_list))
  # table = TransmissionsTable(queryset_list)

  # RequestConfig(request).configure(table)

  # context = {
  #   'table': table
  # }
  # return render(request, 'analysis/transmissions.html', context)

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

    extra_serie = {
      "tooltip": {"y_start": "", "y_end": " transmissions"},
      }

    chartdata = {
      'x': radList,
      'y1': radQty,
      'extra1': extra_serie}

    charttype = "pieChart"

    data = {
        'charttype': charttype,
        'chartdata': chartdata,
    }
    #pdb.set_trace()
    return render_to_response('analysis/piechart.html', data)

  

# queryset_list = Transmissions.objects.filter(profile_frequency__gte = 451850000).filter(profile_frequency__lte = 461000000).filter(timestamp_local__gte='2019-07-16 23:51:47+00')
  # queryset_list = Transmissions.objects.filter(profile_frequency = StartFreq)
  # print('Number of records returned = %s' % len(queryset_list))
  # table = TransmissionsTable(queryset_list)

  # RequestConfig(request).configure(table)

  # context = {
  #   'table': table
  # }
  # return render(request, 'analysis/transmissions.html', context)