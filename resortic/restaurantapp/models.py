from django.db import models

# Create your models here.

class restb(models.Model):
    name=models.CharField(max_length=30)
    time=models.CharField(max_length=30)
    ctime=models.CharField(max_length=30)
    non=models.CharField(max_length=30,null=True)
    veg=models.CharField(max_length=30,null=True)
    re_id=models.AutoField(primary_key=True)