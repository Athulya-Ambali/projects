from django.db import models

# Create your models here.

class patientb(models.Model):
    name=models.CharField(max_length=30)
    address=models.CharField(max_length=30)
    date=models.CharField(max_length=30)
    department=models.CharField(max_length=30)
    disease=models.CharField(max_length=30)
    pa_id=models.AutoField(primary_key=True)