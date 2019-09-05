from __future__ import unicode_literals
from djongo import models



class historial(models.Model):
    #id = models.AutoField(primary_key=True)
    PEDIDO_NUMBER=models.CharField(max_length=100, primary_key = True)
    NOMBRE_PRODUCTO=models.CharField(max_length=100)
    DESCRIPCION_DEL_PRODUCTO=models.CharField(max_length=100)
    ANIO = models.CharField(max_length=100)
    MES = models.CharField(max_length=100)
    DIA = models.CharField(max_length=100)
    HORA = models.CharField(max_length=100)
    PEDIDOS_POR_MES = models.CharField(max_length=100)
    GANANCIA_POR_PLATO = models.CharField(max_length=100)