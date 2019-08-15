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
        fields = '__all__'
class ProductoSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Producto
        fields = ['Categoria', 'Nombre', 'Precio', 'IsBebida', 'IsPlato', 'Descripcion', 'Foto']


class Detalle_orden_menuSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Detalle_orden_menu
        fields = ['Orden_Menu', 'Producto', 'Descripcion']

class ComboSerializer(serializers.ModelSerializer):
    class Meta:
        model = Combo
        fields = '__all__'


class ComboProductoSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = ComboProducto
        fields = ['IsCombo', 'Combo', 'Producto']

class ConsumidorSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Consumidor
        fields = ['Consumidor_id']


class Orden_MenuSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Orden_Menu
        fields = ['Cliente', 'Fecha','Total']

class CategoriaSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Categoria
        fields = ['Nombre','Descripcion']
