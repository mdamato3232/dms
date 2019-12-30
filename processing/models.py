from django.db import models
from assets.models import Component, Sector

# Table holds user specific data displayed on the dashboard
# class UserData(models.model):
    


# Table holds description of the mission
class MissionData(models.Model):
    description = models.CharField(max_length=100)
    username = models.CharField(max_length=150, null=True)
    collection_plan = models.CharField(max_length=100)
    cbp_component = models.ForeignKey('assets.Component',on_delete=models.PROTECT)
    cbp_sector = models.ForeignKey('assets.Sector',on_delete=models.PROTECT)
    sensor = models.CharField(max_length=100)
    tx_fn = models.FileField(upload_to='exports/')
    uploaded_at = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return str(self.id)

# Table holds transmission data elements collected
class Transmissions(models.Model):
    profile_id = models.IntegerField(null=True)
    profile_frequency = models.IntegerField(null=True)
    radio_type = models.CharField(max_length=50,null=True)
    baud_rate = models.SmallIntegerField(null=True)
    bandwidth = models.SmallIntegerField(null=True)
    encryption_type = models.CharField(max_length=50,null=True)
    privacy_method = models.CharField(max_length=50,null=True)
    privacy_id = models.CharField(max_length=50, null=True)
    key = models.CharField(max_length=50,null=True)
    key_id = models.CharField(max_length=50,null=True)
    key_confidence = models.DecimalField(max_digits=4,decimal_places=1,null=True)
    key_set = models.CharField(max_length=50,null=True)
    key_id_set = models.CharField(max_length=50,null=True)
    key_confidence_set = models.CharField(max_length=50,null=True)
    base_mobile = models.CharField(max_length=10,null=True)
    link_id = models.IntegerField(null=True)
    analysis_state = models.CharField(max_length=20,null=True)
    first_timestamp_gmt = models.DateTimeField(null=True)
    first_timestamp_local = models.DateTimeField(null=True)
    latest_timestamp_gmt = models.DateTimeField(null=True)
    latest_timestamp_local = models.DateTimeField(null=True)
    profile_name = models.CharField(max_length=50,null=True)
    profile_comment = models.CharField(max_length=500,null=True)
    profile_action = models.CharField(max_length=50,null=True)
    df_flag = models.NullBooleanField(null=True)
    priority = models.SmallIntegerField(null=True)
    transmission_count = models.IntegerField(null=True)
    highlight_color = models.CharField(max_length=50,null=True)
    alert = models.CharField(max_length=50,null=True)
    audio_device = models.CharField(max_length=50,null=True)
    collect_limit = models.CharField(max_length=10, null=True)
    audio_limit = models.CharField(max_length=10, null=True)
    unplayed_count = models.SmallIntegerField(null=True)
    user_modified = models.CharField(max_length=50,null=True)
    radio_id_from_rule = models.CharField(max_length=50,null=True)
    generate_audio_files = models.CharField(max_length=20,null=True)
    has_audio_flag = models.CharField(max_length=5,null=True)
    audio_file_frequency = models.CharField(max_length=20,null=True)
    case_notation = models.CharField(max_length=80,null=True)
    classification = models.CharField(max_length=80,null=True)
    category1 = models.CharField(max_length=80,null=True)
    category2 = models.CharField(max_length=80,null=True)
    category3 = models.CharField(max_length=80,null=True)
    category4 = models.CharField(max_length=80,null=True)
    category5 = models.CharField(max_length=80,null=True)
    category6 = models.CharField(max_length=80,null=True)
    category7 = models.CharField(max_length=80,null=True)
    category8 = models.CharField(max_length=80,null=True)
    transmission_id = models.IntegerField(null=True)
    transmission_frequency = models.IntegerField(null=True)
    time_slot = models.SmallIntegerField(null=True)
    time_offset = models.IntegerField(null=True)
    transmission_key = models.CharField(max_length=50,null=True)
    transmission_key_id = models.CharField(max_length=25, null=True)
    transmission_key_confidence = models.CharField(max_length=10, null=True)
    content_type = models.CharField(max_length=20,null=True)
    radio_id = models.CharField(max_length=10,null=True)
    coder_id = models.CharField(max_length=10,null=True)
    contact_id = models.CharField(max_length=10,null=True)
    emitter_name = models.CharField(max_length=20,null=True)
    content = models.CharField(max_length=1000,null=True)
    timestamp_gmt = models.DateTimeField(null=True)
    timestamp_local = models.DateTimeField(null=True)
    duration = models.DecimalField(max_digits=6,decimal_places=2,null=True)
    rssi = models.DecimalField(max_digits=5,decimal_places=1,null=True)
    sensor_ip_address = models.CharField(max_length=20,null=True)
    gps_source = models.CharField(max_length=25,null=True)
    sensor_heading_status = models.CharField(max_length=25,null=True)
    sensor_latitude = models.DecimalField(max_digits=10,decimal_places=6,null=True)
    sensor_longitude = models.DecimalField(max_digits=10,decimal_places=6,null=True)
    sensor_elevation = models.DecimalField(max_digits=6,decimal_places=1,null=True)
    sensor_speed = models.DecimalField(max_digits=6,decimal_places=1,null=True)
    sensor_heading = models.DecimalField(max_digits=6,decimal_places=1,null=True)
    sensor_hdop = models.DecimalField(max_digits=4,decimal_places=1,null=True)
    sensor_satellites = models.SmallIntegerField(null=True)
    emitter_latitude = models.DecimalField(max_digits=10,decimal_places=6,null=True)
    emitter_longitude = models.DecimalField(max_digits=10,decimal_places=6,null=True)
    emitter_elevation = models.DecimalField(max_digits=6,decimal_places=1,null=True)
    emitter_speed = models.DecimalField(max_digits=6,decimal_places=1,null=True)
    emitter_heading = models.DecimalField(max_digits=6,decimal_places=1,null=True)
    emitter_gps_accuracy = models.DecimalField(max_digits=4,decimal_places=1,null=True)
    df_orientation = models.SmallIntegerField(null=True)
    df_lob = models.SmallIntegerField(null=True)
    rcf_state = models.CharField(max_length=50,null=True)
    rcf_path = models.CharField(max_length=200,null=True)
    audio_file_state = models.CharField(max_length=50,null=True)
    audio_file_path = models.CharField(max_length=200,null=True)
    transmission_name = models.CharField(max_length=100,null=True)
    transmission_comment = models.CharField(max_length=500,null=True)
    user_defined_text = models.CharField(max_length=500,null=True)
    mission = models.ForeignKey('MissionData',on_delete=models.CASCADE)

    # class Meta:
    #     indexes = [
    #         models.Index(fields=['mission'], name='mission_idx'),
    #     ]
