from django.db import models

# Create your models here.

class vazhitb(models.Model):
    name=models.CharField(max_length=30)
    price=models.CharField(max_length=30)
    vazhi_id=models.AutoField(primary_key=True)