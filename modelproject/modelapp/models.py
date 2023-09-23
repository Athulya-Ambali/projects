from django.db import models

# Create your models here.

class modetb(models.Model):
    name=models.CharField(max_length=30)
    address=models.CharField(max_length=30)
    email=models.CharField(max_length=30)
    mod_id=models.AutoField(primary_key=True)