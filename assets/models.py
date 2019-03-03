from django.db import models

class Components(models.Model):
    component = models.CharField(max_length=5)
    def __str__(self):
        return self.component

class Sectors(models.Model):
    sector = models.CharField(max_length=5)
    def __str__(self):
        return self.sector
    class Meta:
        ordering = ["sector"]

class Asset(models.Model):
  partnumber = models.CharField(max_length=200)
  serialnumber = models.CharField(max_length=200)
  description = models.TextField(blank=True)
  cbp_component = models.ForeignKey(Components,on_delete=models.DO_NOTHING)
  cbp_sector = models.ForeignKey(Sectors,on_delete=models.DO_NOTHING)
  acquire_date = models.DateField(blank=True)
  cost = models.IntegerField(blank=True)
  photo_main = models.ImageField(upload_to='photos/%y/%m/%d')
  photo_1 = models.ImageField(upload_to='photos/%y/%m/%d',blank=True)
  photo_2 = models.ImageField(upload_to='photos/%y/%m/%d',blank=True)
  photo_3 = models.ImageField(upload_to='photos/%y/%m/%d',blank=True)
  photo_4 = models.ImageField(upload_to='photos/%y/%m/%d',blank=True)
  photo_5 = models.ImageField(upload_to='photos/%y/%m/%d',blank=True)
  photo_6 = models.ImageField(upload_to='photos/%y/%m/%d',blank=True)
  website = models.URLField(blank=True)
  configuration = models.FileField(upload_to='files/%y/%m/%d',blank=True)
  def __str__(self):
    return self.partnumber



  


