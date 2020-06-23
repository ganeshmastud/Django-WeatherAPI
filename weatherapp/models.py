from django.db import models

# Create your models here.
class City(models.Model):
    name= models.CharField(max_length=40, blank=False,default= False)
    temperature=models.FloatField(blank=False,default=False)
    feels_like=models.FloatField(blank=False,default=False)
    min_temp=models.FloatField(blank=False,default=False)
    max_temp=models.FloatField(blank=False,default=False)
    description=models.CharField(max_length=40,blank=False,default=False)
    icon=models.CharField(max_length=40,blank=False,default=False)
    def __str__(self):
        return self.name
