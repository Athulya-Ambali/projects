from django.db import models

# Create your models here.

class festtb(models.Model):
    name=models.CharField(max_length=30)
    time=models.CharField(max_length=30)
    description=models.CharField(max_length=30)
    fest_id=models.AutoField(primary_key=True)