from django.db import models

# Create your models here.
class Cliente(models.Model):
    Nombre = models.CharField(max_length=10)
    Apellido = models.CharField(max_length=10)
    Edad = models.CharField(max_length=3)
    Ciudad = models.CharField(max_length=10)


    pub_date = models.DateTimeField('date published')

