from django.db import models

# Create your models here.
class Customer(models.Model):
	firstname=models.CharField(max_length=20,default='firstname')
	lastname=models.CharField(max_length=20,verbose_name='Surname',blank=True)
	address=models.CharField(max_length=20)
	