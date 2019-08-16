radio_type_choices=[
  ('','---'),
  ('P25Phase1','P25Phase1'),
  ('Clear','Clear'),
  ('Dmr','Dmr'),
  ('FixedInversion','FixedInversion'),
  ('LTR','LTR'),
  ('Mpt1327','Mpt1327'),
  ('Nxdn','Nxdn'),
  ('Pager','Pager'),
  ('UnknownRadio','UnknownRadio'),
]

encryption_type_choices = [
  ('','---'),
  ('AES','AES'),
  ('ClearType','ClearType'),
  ('DES','DES'),
  ('Encrypted','Encrypted'),
  ('MototrboEnhanced','MototrboEnhanced'),
  ('Multiple','Multiple'),
]

privacy_method_choices = [
  ('','---'),
  ('Cdcss','Cdcss'),
  ('Ctcss','Ctcss'),
  ('DmrCC','DmrCC'),
  ('NxdnRan','NxdnRan'),
  ('P25Nac','P25Nac'),
]

base_mobile_choices = [
  ('','---'),
  ('BS','BS'),
  ('MS','MS'),
]

rssi_min_choices = [
  ('','---'),
  # ('-110','-110'),
  # ('-100','-100'),
  # ('-90','-90'),
  # ('-80','-80'),
  # ('-70','-70'),
  # ('-60','-60'),
  ('-50','-50'),
  ('-40','-40'),
  ('-30','-30'),
  ('-20','-20'),
  ('-10','-10'),
]