# tutorial/tables.py
import django_tables2 as tables
from .models import Asset
from django_tables2.utils import A


class AssetTable(tables.Table):
    id = tables.LinkColumn('asset', args=[A('pk')])
    class Meta: 
        model = Asset
        # attrs = {'class': 'assettable'}
        exclude = ('description','photo_2','photo_3','file_2','file_3') # fields to exclude
        template_name = 'django_tables2/bootstrap4.html'