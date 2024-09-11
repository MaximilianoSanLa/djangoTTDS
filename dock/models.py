from django.db import models
class vuelos(models.Model):
    idVuelo=models.AutoField(max_length=None,primary_key=True)
    nombre=models.CharField(max_length=255)
    tipo= models.CharField(max_length=15)
    precio=models.IntegerField()
