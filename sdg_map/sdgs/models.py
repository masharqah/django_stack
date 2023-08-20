from django.db import models

# Create your models here.

class Point(models.Model):
    Project_name=models.CharField(max_length=250)
    area = models.CharField(max_length=250)
    partner_name=models.CharField(max_length=250)
    sdgs=models.CharField(null=False, max_length=200, default='None')
    longitude = models.FloatField(default=0)
    latitude = models.FloatField(default=0)

    