from django.shortcuts import render, render_to_response
from processing.models import MissionData, Transmissions
from django_tables2 import RequestConfig
from .tables import MissionDataTable, TransmissionsTable
from collections import Counter
from .forms import QueryForm
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
from django.contrib import messages
from analysis.choices import radio_type_choices, encryption_type_choices, privacy_method_choices, base_mobile_choices, rssi_min_choices
from django.db.models import Max, Min, Count
import time, pdb, json


def index(request):
  return render(request, 'analysis/analysis.html')

def deleteMission(request, mission_id):

    # mission = request.GET.get('mission_id')
    # pdb.set_trace()

    MissionData.objects.filter(pk=mission_id).delete()
    #<input type="submit" onclick="return confirm('Are you sure?')" />
    return HttpResponseRedirect('/analysis')

# Database Query
def dbquery(request):
  # if this is a POST request we need to process the form data
  if request.method == 'POST':
    # create a form instance and populate it with data from the request:
    form = QueryForm(request.POST)
    # check whether it's valid:
    if form.is_valid():
        # Start building the transmissions query based on the form responses
        queryset_list = Transmissions.objects.order_by('timestamp_gmt')

        # Frequency range
        start_freq = form.cleaned_data['start_freq']
        if start_freq:
          start_freq = int(start_freq * 1000000)
          end_freq = form.cleaned_data['end_freq']
          if end_freq:
            end_freq = int(end_freq * 1000000)
            print('end_freq multiplied = %s' % end_freq)
          else:
            end_freq = start_freq
          queryset_list = queryset_list \
            .filter(profile_frequency__gte=start_freq) \
            .filter(profile_frequency__lte=end_freq)

        # Time range
        start_time = form.cleaned_data['start_time']
        if start_time:
          end_time = form.cleaned_data['end_time']
          if not end_time:
            end_time = start_time
          queryset_list = queryset_list \
            .filter(timestamp_local__gte=start_time) \
            .filter(timestamp_local__lte=end_time)
        
        # Mission number
        mission = form.cleaned_data['mission']
        print('Mission Number = %s' % mission)
        if mission:
          queryset_list = queryset_list.filter(mission_id=mission)

        # Privacy ID
        privacy_id = form.cleaned_data['privacy_id']
        print('privacy_id Number = %s' % privacy_id)
        if privacy_id:
          queryset_list = queryset_list.filter(privacy_id=privacy_id)

        # Key
        key = form.cleaned_data['key']
        print('key Number = %s' % key)
        if key:
          queryset_list = queryset_list.filter(key=key)

        # Contact ID
        contact_id = form.cleaned_data['contact_id']
        print('contact_id Number = %s' % contact_id)
        if contact_id:
          queryset_list = queryset_list.filter(contact_id=contact_id)

        # Dropdowns will not be None when empty. Treat differently.
        # Radio Type
        radio_type = form.cleaned_data['radio_type']
        if radio_type != '':
          print('radio_type = %s' % radio_type)
          queryset_list = queryset_list.filter(radio_type=radio_type)

        # Encryption Type
        encryption_type = form.cleaned_data['encryption_type']
        if encryption_type != '':
          print('encryption_type = %s' % encryption_type)
          queryset_list = queryset_list.filter(encryption_type=encryption_type)

        # Privacy Method
        privacy_method = form.cleaned_data['privacy_method']
        if privacy_method != '':
          print('privacy_method = %s' % privacy_method)
          queryset_list = queryset_list.filter(privacy_method=privacy_method)

        # Base/Mobile
        base_mobile = form.cleaned_data['base_mobile']
        if base_mobile != '':
          print('base_mobile = %s' % base_mobile)
          queryset_list = queryset_list.filter(base_mobile=base_mobile)

        # Minimum RSSI filter
        rssi_min = form.cleaned_data['rssi_min']
        if rssi_min != ('' or None):
          print('rssi_min = %s' % rssi_min)
          queryset_list = queryset_list.filter(rssi__gte=rssi_min)



        # Alerts
        if not queryset_list:
          messages.error(request, 'No records match search parameters')
          return HttpResponseRedirect('#')
        numRecords = len(queryset_list)
        print('Number of records returned = %s' % numRecords)
        messages.success(request, 'Number of records returned = %s' % numRecords)


        table = TransmissionsTable(queryset_list) # Instantiate Table

        RequestConfig(request).configure(table) # Configure Table

        # Get dataset ready for radio pie chart.
        radio_dataset = queryset_list \
          .values('radio_type') \
          .exclude(radio_type='') \
          .annotate(total=Count('radio_type')) \
          .order_by('radio_type')
        
        chart = list(map(lambda row: {'name': row['radio_type'], \
              'y': row['total']}, radio_dataset))
        # pdb.set_trace()
        context = {
          'table': table,
          'chart': chart,
          'numRecords': numRecords
        }
        return render(request, 'analysis/analysis.html', context)
    else: 
      messages.error(request, 'Empty Form')
      return HttpResponseRedirect('#')

        # # redirect to a new URL:
        # return HttpResponseRedirect('/analysis/')

  # if a GET (or any other method) we'll create a blank form
  else:
      form = QueryForm()
      context = {
        'form': form,
      }
  return render(request, 'analysis/dbqueryform.html', context)





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
#     #return render(request, 'letcap/piechart.html', data)
#     return render_to_response('letcap/piechart.html', data)

def radiopie(request, mission_id):
    # mission = request.GET.get('miss_id')
    l = Transmissions.objects.filter(mission=mission_id).values('radio_type')
    radios = [d['radio_type'] for d in l]
    radList = list(Counter(radios).keys())
    radQty = list(Counter(radios).values())
    # pdb.set_trace()
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

    ######################################################################

# HighCharts try...

def process_query(request, mission_id):
  return render(request, 'analysis/jsonpiechart.html')

def radiopie2(request):
  dataset = Transmissions.objects.filter(mission=92) \
    .values('radio_type') \
    .exclude(radio_type='') \
    .annotate(total=Count('radio_type')) \
    .order_by('radio_type')

  chart = {
    'chart': {'type': 'pie'},
    'title': {'text': 'Transmissions by Radio Type'},
    'series': [{
        'name': 'Transmissions',
        'data': list(map(lambda row: {'name': row['radio_type'], 'y': row['total']}, dataset))
    }]
  }
  # pdb.set_trace()
  return JsonResponse(chart)

  # l = Transmissions.objects.filter(mission=mission_id).values('radio_type')
  # radios = [d['radio_type'] for d in l]
  # radList = list(Counter(radios).keys())
  # radQty = list(Counter(radios).values())
  # # pdb.set_trace()
  # extra_serie = {
  #   "tooltip": {"y_start": "", "y_end": " transmissions"},
  #   }

  # chartdata = {
  #   'x': radList,
  #   'y1': radQty,
  #   'extra1': extra_serie}

  # charttype = "pieChart"

  # data = {
  #     'charttype': charttype,
  #     'chartdata': chartdata,
  # }
  # #pdb.set_trace()
  # return render_to_response('analysis/piechart.html', data)

  

# queryset_list = Transmissions.objects.filter(profile_frequency__gte = 451850000).filter(profile_frequency__lte = 461000000).filter(timestamp_local__gte='2019-07-16 23:51:47+00')
  # queryset_list = Transmissions.objects.filter(profile_frequency = StartFreq)
  # print('Number of records returned = %s' % len(queryset_list))
  # table = TransmissionsTable(queryset_list)

  # RequestConfig(request).configure(table)

  # context = {
  #   'table': table
  # }
  # return render(request, 'analysis/trfor 