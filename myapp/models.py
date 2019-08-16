from django.db import models
from datetime import datetime


# Create your models here.
class Contacto(models.Model):
    Nombre = models.CharField(max_length=30)
    Email = models.CharField(max_length=20)
    Ciudad = models.CharField(max_length=10)
    Asunto = models.CharField(max_length=20)
    Fecha_Nacimiento = models.DateField
    Mensaje = models.CharField(max_length=1000)

    def __str__(self):
        return self.Nombre


class Persona(models.Model):
    Persona_id = models.AutoField(primary_key=True)
    Contacto = models.ForeignKey(Contacto, on_delete=models.CASCADE)


class Cliente(Persona):
    Nombre = models.CharField(max_length=10)
    Apellido = models.CharField(max_length=10)
    Edad = models.CharField(max_length=3)
    Ciudad = models.CharField(max_length=10)
    Correo = models.CharField(max_length=20)

    def __str__(self):
        return self.Nombre


class Consumidor(Persona):
    Consumidor_id = models.AutoField(primary_key=True)


class Orden_Menu(models.Model):
    Cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)
    Fecha = models.DateField(default=datetime.now)
    Total = models.DecimalField(max_digits=6, decimal_places=2)


class Categoria(models.Model):
    Nombre = models.CharField(max_length=20)
    Descripcion = models.CharField(max_length=30)

    def __str__(self):
        return self.Nombre


class Producto(models.Model):
    Categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE)
    Nombre = models.CharField(max_length=30)
    Precio = models.DecimalField(max_digits=4, decimal_places=2)
    IsBebida = models.BooleanField()
    IsPlato = models.BooleanField()
    Descripcion = models.CharField(max_length=800)
    Foto = models.ImageField

    def __str__(self):
        return self.Nombre


class Detalle_orden_menu(models.Model):
    Orden_Menu = models.ForeignKey(Orden_Menu, on_delete=models.CASCADE)
    Producto = models.ForeignKey(Producto, on_delete=models.CASCADE)
    Descripcion = models.CharField(max_length=800)


class Combo(models.Model):
    Descripcion = models.CharField(max_length=30)
    Precio = models.DecimalField(max_digits=4, decimal_places=2)

    def __str__(self):
        return self.Descripcion


class ComboProducto(models.Model):
    IsCombo = models.BooleanField()
    Combo = models.ForeignKey(Combo, on_delete=models.CASCADE)
    Producto = models.ForeignKey(Producto, on_delete=models.CASCADE)
