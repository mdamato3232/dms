# tutorial/tables.py
import django_tables2 as tables
from .models import Asset
from django_tables2.utils import A
from django.contrib.humanize.templatetags.humanize import intcomma

class ColumnWithIntComma(tables.Column):
    def render(self,value):
        return intcomma(value)

class CurrencyColumn(tables.Column):
    def render(self,value):
        return "$" + str(intcomma(value))

class AssetTable(tables.Table):
    id = tables.LinkColumn('asset', args=[A('pk')])
    partnumber = tables.LinkColumn('asset', args=[A('pk')])
    serialnumber = tables.Column()
    component = tables.Column()
    sector = tables.Column()
    acquire_date = tables.Column()
    cost = CurrencyColumn()
    photo_main = tables.Column()

    class Meta: 
        # model = Asset # if you want to display every column (exclude below)
        # attrs = {'class': 'assettable'} # if you want to assign a class for css
        # # exclude = ('description','photo_1','photo_2','photo_3','photo_4','photo_5','photo_6',
        # #     'file_1','file_2','file_3','file_4','file_5','file_6', 'website') # fields to exclude
        template_name = 'django_tables2/bootstrap4.html'