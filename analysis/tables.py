# tutorial/tables.py
import django_tables2 as tables
from processing.models import MissionData
from django_tables2.utils import A
from django.contrib.humanize.templatetags.humanize import intcomma

class ColumnWithIntComma(tables.Column):
    def render(self,value):
        return intcomma(value)

class CurrencyColumn(tables.Column):
    def render(self,value):
        return "$" + str(intcomma(value))

class MissionDataTable(tables.Table):
    id = tables.LinkColumn('asset', args=[A('pk')])
    description = tables.Column()
    name = tables.Column()
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