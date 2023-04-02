from django.db import models

# Create your models here.

class City_Info(models.Model):
    City= models.CharField(max_length=50,primary_key=True)
    Population=models.IntegerField()