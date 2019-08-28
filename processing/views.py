from django.shortcuts import render
from .forms import UploadFileForm
from letcdms import settings
from django.http import HttpResponse, HttpResponseRedirect
import psycopg2
import re
from django.contrib import messages
import pdb, csv

drtTransHeaders = ['ProfileId', 'ProfileFrequency', 'RadioModel', 'Baud',
                    'Bandwidth', 'Encryption', 'PrivacyModel', 'PrivacyId',
                    'Key', 'KeyId', 'KeyConfidence', 'KeySet', 'KeyIdSet',
                    'KeyConfidenceSet', 'Link', 'LinkId', 'State',
                    'FirstTimestamp', 'FirstTimestampLocal',
                    'LatestTimestamp', 'LatestTimestampLocal', 'ProfileName',
                    'ProfileComment', 'Action', 'DF', 'Priority',
                    'Count', 'Color', 'Alert', 'AudioDevice', 'CollectLimit', 
                    'AudioLimit', 'UnplayedTransmissionCount', 'UserModified',
                    'RadioIdFromRule', 'GenerateAudioFiles', 'HasAudio',
                    'AudioFileFrequency', 'CaseNotation', 'Classification', 
                    'Category1', 'Category2', 'Category3', 'Category4', 
                    'Category5', 'Category6', 'Category7', 'Category8',
                    'TransmissionId', 'TransmissionFrequency', 'TimeSlot',
                    'TimeOffset', 'TransmissionKey', 'TransmissionKeyId',
                    'TransmissionKeyConfidence', 'ContentType', 'RadioId',
                    'CoderId', 'ContactId', 'EmitterName', 'Content',
                    'Timestamp', 'TimestampLocal', 'Duration', 'Rssi',
                    'DrtUnitAddress', 'DrtGpsSource', 'DrtHeadingStatus',
                    'DrtLatitude', 'DrtLongitude', 'DrtElevation', 'DrtSpeed',
                    'DrtHeading', 'DrtHdop', 'DrtSatellites',
                    'EmitterLatitude', 'EmitterLongitude', 'EmitterElevation',
                    'EmitterSpeed', 'EmitterHeading', 'EmitterGpsAccuracy',
                    'DfOrientation', 'DfLob', 'RcfState', 'RcfPath',
                    'AudioFileState', 'AudioFilePath', 'TransmissionName',
                    'TransmissionComment', 'UserDefined'] 

transHeaders = ['profile_id', 'profile_frequency', 'radio_type', 'baud_rate', 
                'bandwidth', 'encryption_type', 'privacy_method', 'privacy_id',
                'key', 'key_id', 'key_confidence', 'key_set', 'key_id_set', 
                'key_confidence_set', 'base_mobile', 'link_id',
                'analysis_state', 'first_timestamp_gmt',
                'first_timestamp_local', 'latest_timestamp_gmt',
                'latest_timestamp_local', 'profile_name',
                'profile_comment', 'profile_action', 'df_flag', 'priority',
                'transmission_count', 'highlight_color', 'alert',
                'audio_device', 'collect_limit', 'audio_limit',
                'unplayed_count', 'user_modified', 'radio_id_from_rule',
                'generate_audio_files', 'has_audio_flag','audio_file_frequency',
                'case_notation', 'classification', 'category1', 'category2',
                'category3', 'category4', 'category5', 'category6', 'category7',
                'category8', 'transmission_id', 'transmission_frequency',
                'time_slot', 'time_offset', 'transmission_key',
                'transmission_key_id', 'transmission_key_confidence',
                'content_type', 'radio_id', 'coder_id', 'contact_id',
                'emitter_name', 'content', 'timestamp_gmt', 'timestamp_local',
                'duration', 'rssi', 'sensor_ip_address', 'gps_source',
                'sensor_heading_status', 'sensor_latitude', 'sensor_longitude',
                'sensor_elevation', 'sensor_speed', 'sensor_heading',
                'sensor_hdop', 'sensor_satellites', 'emitter_latitude',
                'emitter_longitude', 'emitter_elevation', 'emitter_speed',
                'emitter_heading', 'emitter_gps_accuracy', 'df_orientation',
                'df_lob', 'rcf_state', 'rcf_path', 'audio_file_state',
                'audio_file_path', 'transmission_name', 'transmission_comment',
                'user_defined_text','mission_id']

def index(request):
  return render(request, 'processing/processing.html')

def upload(request):
    if request.method == 'POST':
        form = UploadFileForm(request.POST, request.FILES)
        if form.is_valid():
            newform = form.save(commit=False)
            newform.username = request.user.username # Insert login name
            newform.save() # write record to database missiondata table
            # ingest transmission data into database
            if newform.tx_fn:
                rc = ingest(settings.MEDIA_ROOT+'/'+str(newform.tx_fn),newform.pk)
                if rc == None:
                    messages.success(request, 'Mission ' + str(newform.pk) + ' Data Successfully Ingested')
                else:
                    messages.error(request, 'Mission ' + str(newform.pk) +
                        ' Error during Ingest code = %s' % rc)
            return HttpResponseRedirect('/processing/')
    else:
        form = UploadFileForm()
    return render(request, 'processing/processing.html', {'form': form})

def ingest(filename,primarykey):
    # establish connection with database.
    conn = psycopg2.connect("host=localhost dbname=letcdb user=mike password=radio")
    cur = conn.cursor()
    # read the first line, profile?, transmission?, or neither
    with open(filename, newline='') as csvfile:
        inputreader = csv.reader(csvfile,dialect='excel')
        firstLine = next(inputreader)
        if 'Transmission' in firstLine[0]:
            transmission = exportloader(inputreader, transHeaders, drtTransHeaders, filename, primarykey)
            print ('Transmission file name in /tmp = %s' % transmission)
            with open(transmission,'r') as f:
                next(f) # read past the line with the column names.
                rc = None
                # This is really ugly but necessary because cur.copy does not
                # handle quoted strings properly.
                try:
                    cur.copy_expert("COPY processing_transmissions (profile_id, profile_frequency, \
                        radio_type, baud_rate, \
                        bandwidth, encryption_type, privacy_method, privacy_id,\
                        key, key_id, key_confidence, key_set, key_id_set, \
                        key_confidence_set, base_mobile, link_id,\
                        analysis_state, first_timestamp_gmt,\
                        first_timestamp_local, latest_timestamp_gmt,\
                        latest_timestamp_local, profile_name,\
                        profile_comment, profile_action, df_flag, priority,\
                        transmission_count, highlight_color, alert,\
                        audio_device, collect_limit, audio_limit,\
                        unplayed_count, user_modified, radio_id_from_rule,\
                        generate_audio_files, has_audio_flag,audio_file_frequency,\
                        case_notation, classification, category1, category2,\
                        category3, category4, category5, category6, category7,\
                        category8, transmission_id, transmission_frequency,\
                        time_slot, time_offset, transmission_key,\
                        transmission_key_id, transmission_key_confidence,\
                        content_type, radio_id, coder_id, contact_id,\
                        emitter_name, content, timestamp_gmt, timestamp_local,\
                        duration, rssi, sensor_ip_address, gps_source,\
                        sensor_heading_status, sensor_latitude, sensor_longitude,\
                        sensor_elevation, sensor_speed, sensor_heading,\
                        sensor_hdop, sensor_satellites, emitter_latitude,\
                        emitter_longitude, emitter_elevation, emitter_speed,\
                        emitter_heading, emitter_gps_accuracy, df_orientation,\
                        df_lob, rcf_state, rcf_path, audio_file_state,\
                        audio_file_path, transmission_name, transmission_comment,\
                        user_defined_text,mission_id) FROM STDIN WITH DELIMITER ','  CSV", f)
                except psycopg2.DataError as e:
                    print('DataError  %s ' % e)
                    rc = 1 #error code 1 DB error
                except:
                    print('Unknown error writing file %s to database' % transmission)
                    rc = 1 #error code 1 DB error
            if rc == None:
                conn.commit()
            f.close()
        else:
            print('Unknown file format')
            rc = 100
        csvfile.close()
        return rc

# exportloader creates the temporary (/tmp) csv file needed for import to db.
def exportloader(inputrdr, headers, drtHeaders, originalName, primaryKey):
    # get the original filename
    match = re.search(r'exports/(.*$)',originalName)
    if match:
        newName = '/tmp/new' + match.group(1)
        print('The new name of the file is: %s' % newName)
    with open(newName, 'w', newline='') as csvfileout:
        outputwriter = csv.writer(csvfileout,dialect='excel')
        # first row of .csv file is the list of labels defining data elements.
        outputwriter.writerow(headers)
        # find out which elements are in the input file and get their indexes.
        fields = []
        # secondLine in DRT export file has all the field names,read into list.
        secondLine = next(inputrdr)
        i = 0 # counter for source file column
        for element in secondLine: # loop over elements and look for them 
            index = find_element_in_list(element,drtHeaders)
            if index != None:
                print("matches index=%s, element = %s" % (index, element))
                tupleIndex = (index, i) # tuple (destinationIndex, SourceIndex)
                fields.append(tupleIndex) # save one tuple per found element.
            else:
                print(10*'-' + '>' +"No match: %s" % element) #Ignore Elements.
            i += 1 # Increment source file column index
        # Now, copy data from source file to destination file row by row.
        rowCount = 0
        for newLine in inputrdr:
            newRow = []
            for i in range(len(headers)-1): # create a blank list -1 for pk.
                newRow.append('')
            for i in fields: # fields is a list of tuples (dest, source)
                newRow[i[0]] = newLine[i[1]] # copy i[0]-dest, i[1]-source
            # add the primary key to the last element in the list.
            newRow.append(str(primaryKey))
            try:
                outputwriter.writerow(newRow)
            except TypeError:
                print('TypeError writing newRow rowCount= %s' % rowCount)
            except:
                print('Error writing newRow rowCount = %s' % rowCount)
            rowCount += 1
    csvfileout.close()
    return newName # return the name of the temporary file.

# Quick utility to return index of found element in a list.
def find_element_in_list(element, listofelements):
    try:
        index_element = listofelements.index(element)
        return index_element
    except: ValueError
    return None
