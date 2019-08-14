from django import forms

class QueryForm(forms.Form):
  start_freq = forms.DecimalField(max_digits=8,decimal_places=4)
  end_freq = forms.DecimalField(max_digits=8,decimal_places=4,required=False)
  start_time = forms.DateTimeField(required=False)
  end_time = forms.DateTimeField(required=False)
  radio_type = forms.CharField(max_length=50,required=False)
  encryption_type = forms.CharField(max_length=50,required=False)
  privacy_method = forms.CharField(max_length=50,required=False)
  privacy_id = forms.CharField(max_length=50,required=False)
  key = forms.CharField(max_length=50,required=False)
  base_mobile = forms.CharField(max_length=10,required=False)
  radio_id = forms.CharField(max_length=10,required=False)
  contact_id = forms.CharField(max_length=10,required=False)
  duration_min = forms.DecimalField(max_digits=6,decimal_places=2,required=False)
  duration_max = forms.DecimalField(max_digits=6,decimal_places=2,required=False)
  rssi_min = forms.DecimalField(max_digits=5,decimal_places=1,required=False)
  rssi_max = forms.DecimalField(max_digits=5,decimal_places=1,required=False)





