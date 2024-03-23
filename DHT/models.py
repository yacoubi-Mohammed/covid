from django.db import models

import django.db
class Patient(models.Model):
    #id = models.AutoField(primary_key=True)
    temp = models.FloatField(null=True)
    oxygene_level= models.FloatField(null=True)
    respiratoryRate = models.FloatField(null=True)
    heartRate = models.FloatField(null=True)
    dt = models.DateTimeField(auto_now_add=True,null=True)

