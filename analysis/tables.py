# tutorial/tables.py
import django_tables2 as tables
from processing.models import MissionData, Transmissions
from django_tables2.utils import A
from django.contrib.humanize.templatetags.humanize import intcomma

class ColumnWithIntComma(tables.Column):
    def render(self,value):
        return intcomma(value)

class CurrencyColumn(tables.Column):
    def render(self,value):
        return "$" + str(intcomma(value))

class MissionDataTable(tables.Table):
    # id = tables.Column()
    id = tables.LinkColumn('viewtransmissiondata', args=[A('pk')])
    # description = tables.Column()
    description = tables.LinkColumn('json_example', args=[A('pk')])
    usname = tables.Column()
    collection_plan = tables.Column()
    cbp_component = tables.Column()
    cbp_sector = tables.Column()
    sensor = tables.Column()
    tx_fn = tables.Column()
    uploaded_at = tables.Column()

    class Meta: 
        # model = Asset # if you want to display every column (exclude below)
        # attrs = {'class': 'assettable'} # if you want to assign a class for css
        # # exclude = ('description','photo_1','photo_2','photo_3','photo_4','photo_5','photo_6',
        # #     'file_1','file_2','file_3','file_4','file_5','file_6', 'website') # fields to exclude
        template_name = 'django_tables2/bootstrap4.html'

class TransmissionsTable(tables.Table):
    id = tables.Column()
    profile_id = tables.Column()
    profile_frequency = tables.Column()
    radio_type = tables.Column()
    baud_rate = tables.Column()
    bandwidth = tables.Column()
    encryption_type = tables.Column()
    privacy_method = tables.Column()
    sensor_latitude = tables.Column()
    sensor_longitude = tables.Column()
    key = tables.Column()
    key_id = tables.Column()
    key_confidence = tables.Column()
    base_mobile = tables.Column()
    rssi = tables.Column()
    analysis_state = tables.Column()
    timestamp_local = tables.Column()
    transmission_count = tables.Column()
    mission = tables.Column()

    class Meta: 
        # model = Asset # if you want to display every column (exclude below)
        # attrs = {'class': 'assettable'} # if you want to assign a class for css
        # # exclude = ('description','photo_1','photo_2','photo_3','photo_4','photo_5','photo_6',
        # #     'file_1','file_2','file_3','file_4','file_5','file_6', 'website') # fields to exclude
        template_name = 'django_tables2/bootstrap4.html'        