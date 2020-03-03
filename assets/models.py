from django.db import models
from django.dispatch import receiver
from django.db.models.signals import post_save
import os, pdb
from assets.signals import rotate_image



class Component(models.Model):
    component = models.CharField(max_length=5)
    def __str__(self):
        return self.component

class Sector(models.Model):
    sector = models.CharField(max_length=5)
    def __str__(self):
        return self.sector
    class Meta:
        ordering = ["sector"]

class Asset(models.Model):
  partnumber = models.CharField(max_length=200)
  serialnumber = models.CharField(max_length=200)
  description = models.TextField(blank=True)
  component = models.ForeignKey(Component,on_delete=models.DO_NOTHING)
  sector = models.ForeignKey(Sector,on_delete=models.DO_NOTHING)
  acquire_date = models.DateField(blank=True)
  cost = models.IntegerField(blank=True)
  photo_main = models.ImageField(upload_to='photos/%y/%m/%d')
  photo_1 = models.ImageField(upload_to='photos/%y/%m/%d',blank=True)
  photo_2 = models.ImageField(upload_to='photos/%y/%m/%d',blank=True)
  photo_3 = models.ImageField(upload_to='photos/%y/%m/%d',blank=True)
  photo_4 = models.ImageField(upload_to='photos/%y/%m/%d',blank=True)
  photo_5 = models.ImageField(upload_to='photos/%y/%m/%d',blank=True)
  photo_6 = models.ImageField(upload_to='photos/%y/%m/%d',blank=True)
  file_1 = models.FileField(upload_to='files/%y/%m/%d',blank=True)
  file_2 = models.FileField(upload_to='files/%y/%m/%d',blank=True)
  file_3 = models.FileField(upload_to='files/%y/%m/%d',blank=True)
  file_4 = models.FileField(upload_to='files/%y/%m/%d',blank=True)
  file_5 = models.FileField(upload_to='files/%y/%m/%d',blank=True)
  file_6 = models.FileField(upload_to='files/%y/%m/%d',blank=True)
  website = models.URLField(blank=True)
  is_available = models.BooleanField(default=False)
  def __str__(self):
    return self.partnumber

# method for updating photo rotation.  See signals.py for rotation code.
@receiver(post_save, sender=Asset, dispatch_uid="update_image_asset")
def update_image(sender, instance, **kwargs):
  # pdb.set_trace()
  if instance.photo_main:
    BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    fullpath = BASE_DIR + instance.photo_main.url
    rotate_image(fullpath)
  if instance.photo_1:
    BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    fullpath = BASE_DIR + instance.photo_1.url
    rotate_image(fullpath)
  if instance.photo_2:
    BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    fullpath = BASE_DIR + instance.photo_2.url
    rotate_image(fullpath)
  if instance.photo_3:
    BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    fullpath = BASE_DIR + instance.photo_3.url
    rotate_image(fullpath)
  if instance.photo_4:
    BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    fullpath = BASE_DIR + instance.photo_4.url
    rotate_image(fullpath)
  if instance.photo_5:
    BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    fullpath = BASE_DIR + instance.photo_5.url
    rotate_image(fullpath)
  if instance.photo_6:
    BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    fullpath = BASE_DIR + instance.photo_6.url
    rotate_image(fullpath)
    

  


