from django.db import models

# Create your models here.

class viewtb(models.Model):
    name=models.CharField(max_length=30)
    address=models.CharField(max_length=30)
    email=models.CharField(max_length=30)
    reg_id=models.AutoField(primary_key=True)
