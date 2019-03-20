from django import forms
from .models import MissionData

class UploadFileForm(forms.ModelForm):
    class Meta:
        model = MissionData
        fields = ('description', 'name', 'collection_plan',
            'cbp_component', 'cbp_sector', 'sensor', 'tx_fn', )