from django.shortcuts import render
from processing.models import MissionData, Transmissions
from django_tables2 import RequestConfig
from .tables import MissionDataTable, TransmissionsTable
from collections import Counter
from .forms import QueryForm
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
from django.contrib import messages
from analysis.choices import radio_type_choices, encryption_type_choices, privacy_method_choices, base_mobile_choices, rssi_min_choices
from django.db.models import Max, Min, Count
import time, pdb, json, pickle

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
        if mission:
          queryset_list = queryset_list.filter(mission_id=mission)

        # Privacy ID
        privacy_id = form.cleaned_data['privacy_id']
        if privacy_id:
          queryset_list = queryset_list.filter(privacy_id=privacy_id)

        # Key
        key = form.cleaned_data['key']
        if key:
          queryset_list = queryset_list.filter(key=key)

        # Contact ID
        contact_id = form.cleaned_data['contact_id']
        if contact_id:
          queryset_list = queryset_list.filter(contact_id=contact_id)

        # Dropdowns will not be None when empty. Treat differently.
        # Radio Type
        radio_type = form.cleaned_data['radio_type']
        if radio_type != '':
          queryset_list = queryset_list.filter(radio_type=radio_type)

        # Encryption Type
        encryption_type = form.cleaned_data['encryption_type']
        if encryption_type != '':
          queryset_list = queryset_list.filter(encryption_type=encryption_type)

        # Privacy Method
        privacy_method = form.cleaned_data['privacy_method']
        if privacy_method != '':
          queryset_list = queryset_list.filter(privacy_method=privacy_method)

        # Base/Mobile
        base_mobile = form.cleaned_data['base_mobile']
        if base_mobile != '':
          queryset_list = queryset_list.filter(base_mobile=base_mobile)

        # Minimum RSSI filter
        rssi_min = form.cleaned_data['rssi_min']
        if rssi_min != ('' or None):
          queryset_list = queryset_list.filter(rssi__gte=rssi_min)

        # Alerts
        if not queryset_list:
          messages.error(request, 'No records match search parameters')
          return HttpResponseRedirect('#')

        # pickle the queryset_list 
        # fw = open('/tmp/pickle.dat', 'wb')
        # pickle.dump(queryset_list, fw)
        # fw.close
        #  save this for later...context = setContext(request, queryset_list)

        numRecords = len(queryset_list)
        messages.success(request, 'Number of records returned = %s' % numRecords)

        # Get day of the week info...
       
        days=[]
        for day in range(1,8):
          daycount = queryset_list.filter(timestamp_local__week_day=day).count()
          days.append(daycount)
        print('days = %s' % days)
          
        # Get the first and last timestamps
        timeSet = queryset_list.values('timestamp_gmt').order_by('timestamp_gmt')
        timeSetnv = queryset_list.order_by('timestamp_gmt')

        firstTime = timeSet[0]
        lastTime = timeSet[numRecords-1]
        print('first = %s' % firstTime['timestamp_gmt'])
        print('last = %s' % lastTime['timestamp_gmt'])
        totalTime = lastTime['timestamp_gmt'] - firstTime['timestamp_gmt']
        print('totalTime = %s' % totalTime)

        table = TransmissionsTable(queryset_list.order_by('timestamp_gmt')) # Instantiate Table

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
          'totalTime': totalTime,
          'table': table,
          'chart': chart,
          'numRecords': numRecords,
          'days': days
        }
        return render(request, 'analysis/analysis.html', context)
    else: 
      messages.error(request, 'Empty Form')
      return HttpResponseRedirect('#')

        # # redirect to a new URL:
        # return HttpResponseRedirect('/analysis/')

  # if a GET (or any other method) we'll create a blank form
  else:

    # if request.GET:
    #   print('about to open pickle file')
    #   fd = open('/tmp/pickle.dat', 'rb')
    #   print('about to unpickle')
    #   qs = pickle.load(fd)
    #   print('about to call setContext')
    #   context = setContext(request, qs)
    #   print('about to render')
    #   return render(request, 'analysis/analysis.html', context)
    # else:
    form = QueryForm()
    context = {
      'form': form
    }
    return render(request, 'analysis/dbqueryform.html', context)

###################################################################################
# def setContext(request, qs_list):
  # numRecords = len(qs_list)
  # print('Number of records returned = %s' % numRecords)
  # messages.success(request, 'Number of records returned = %s' % numRecords)
  # Get day of the week info...
  # days=[]
  # for day in range(1,8):
  #   daycount = qs_list.filter(timestamp_local__week_day=day).count()
  #   days.append(daycount)
  # print('days = %s' % days)
  # # Get the first and last timestamps
  # timeSet = qs_list.values('timestamp_gmt').order_by('timestamp_gmt')
  # timeSetnv = qs_list.order_by('timestamp_gmt')
  # firstTime = timeSet[0]
  # lastTime = timeSet[numRecords-1]
  # print('first = %s' % firstTime['timestamp_gmt'])
  # print('last = %s' % lastTime['timestamp_gmt'])
  # totalTime = lastTime['timestamp_gmt'] - firstTime['timestamp_gmt']
  # print('totalTime = %s' % totalTime)
  # table = TransmissionsTable(qs_list.order_by('timestamp_gmt')) # Instantiate Table
  # print('About to instantiate table')
  # table = TransmissionsTable(qs_list) # Instantiate Table
  # print('about to configure table')
  # RequestConfig(request).configure(table) # Configure Table
  # print('about to set context')
  # Get dataset ready for radio pie chart.
  # radio_dataset = qs_list \
  #   .values('radio_type') \
  #   .exclude(radio_type='') \
  #   .annotate(total=Count('radio_type')) \
  #   .order_by('radio_type')
  # chart = list(map(lambda row: {'name': row['radio_type'], \
  #       'y': row['total']}, radio_dataset))
  # pdb.set_trace()
  context = {
    # 'totalTime': totalTime,
    'table': table,
    # 'chart': chart,
    # 'numRecords': numRecords,
    # 'days': days
  }
  # time.sleep(5)
  print('about to return from setContext')
  return context
###################################################################################


 
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
  print('queryset_list is of type: -> ', type(queryset_list))
  print('queryset_list is of length: -> ', len(queryset_list))
  table = TransmissionsTable(queryset_list)
  print(table)
  print('table is of type: -> ', type(table))

  # put some debug print statements to figure out sorting...
  print('request.scheme = %s' % request.scheme)
  print('request.path = %s' % request.path)
  print('request.path_info = %s' % request.path_info)
  print('request.method = %s' % request.method)
  print('request.body = %s' % request.body)
  print('request.GET = %s' % request.GET)
  d = request.GET
  print('length of request.GET dict = %s' % len(request.GET))
  print(d.keys())
  for k in sorted(d.keys()):
    print('Key:', k, '->', d[k])
  mm = request.META
  print('META dict is of length: -> ', len(mm))
  print('META is of type: -> ', type(mm))

  for k in sorted(mm.keys()):
    print('Meta Key:', k, '->', mm[k])

  
  RequestConfig(request).configure(table)

  context = {
    'table': table
  }
  return render(request, 'analysis/transmissions.html', context)

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

  