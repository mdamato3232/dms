from django.db import models

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
  photo_2 = models.ImageField(upload_to='photos/%y/%m/%d',blank=True)
  photo_3 = models.ImageField(upload_to='photos/%y/%m/%d',blank=True)
  file_main = models.FileField(upload_to='files/%y/%m/%d',blank=True)
  file_2 = models.FileField(upload_to='files/%y/%m/%d',blank=True)
  file_3 = models.FileField(upload_to='files/%y/%m/%d',blank=True)
  website = models.URLField(blank=True)
  def __str__(self):
    return self.partnumber



  


