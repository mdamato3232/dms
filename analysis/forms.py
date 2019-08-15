from django import forms
from analysis.choices import radio_type_choices,encryption_type_choices,privacy_method_choices,base_mobile_choices,rssi_min_choices

class QueryForm(forms.Form):
  start_freq = forms.DecimalField(max_digits=8,decimal_places=4,required=False)
  end_freq = forms.DecimalField(max_digits=8,decimal_places=4,required=False)
  start_time = forms.DateTimeField(required=False)
  end_time = forms.DateTimeField(required=False)
  radio_type = forms.CharField(max_length=50,required=False,widget=forms.Select(choices=radio_type_choices))
  encryption_type = forms.CharField(max_length=50,required=False,widget=forms.Select(choices=encryption_type_choices))
  privacy_method = forms.CharField(max_length=50,required=False,widget=forms.Select(choices=privacy_method_choices))
  privacy_id = forms.CharField(max_length=50,required=False)
  key = forms.CharField(max_length=50,required=False)
  base_mobile = forms.CharField(max_length=10,required=False,widget=forms.Select(choices=base_mobile_choices))
  radio_id = forms.CharField(max_length=10,required=False)
  contact_id = forms.CharField(max_length=10,required=False)
  duration_min = forms.DecimalField(max_digits=6,decimal_places=2,required=False)
  duration_max = forms.DecimalField(max_digits=6,decimal_places=2,required=False)
  rssi_min = forms.DecimalField(max_digits=5,decimal_places=1,required=False,widget=forms.Select(choices=rssi_min_choices))
  mission = forms.IntegerField(required=False)





