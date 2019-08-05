from .models import *
from rest_framework import serializers

class ContactoSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Contacto
        fields = ['Nombre', 'Email', 'Ciudad', 'Asunto', 'Fecha_Nacimiento', 'Mensaje']


class PersonaSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Persona
        fields = ['Persona_id', 'Contacto']

class ClienteSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Contacto
        fields = ['Nombre', 'Apellido', 'Edad', 'Ciudad', 'Correo']
class ProductoSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Producto
        fields = ['Categoria', 'Nombre', 'Precio', 'IsBebida', 'IsPlato', 'Descripcion', 'Foto']


class Detalle_orden_menuSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Detalle_orden_menu
        fields = ['Orden_Menu', 'Producto', 'Descripcion']

class ComboSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Combo
        fields = ['Descripcion', 'precio']


class ComboProductoSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = ComboProducto
        fields = ['IsCombo', 'Combo', 'Producto']