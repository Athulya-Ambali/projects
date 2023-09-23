from django.db import models

# Create your models here.

class resortb(models.Model):
    name=models.CharField(max_length=30)
    email=models.CharField(max_length=30)
    contact=models.CharField(max_length=30)
    rooms=models.CharField(max_length=30)
    single=models.CharField(max_length=30,null=True)
    doble=models.CharField(max_length=30,null=True)
    family=models.CharField(max_length=30,null=True)
    sprice=models.CharField(max_length=30)
    dprice=models.CharField(max_length=30)
    fprice=models.CharField(max_length=30)
    price=models.CharField(max_length=30)
    ro_id=models.AutoField(primary_key=True)
    