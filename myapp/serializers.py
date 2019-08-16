from .models import *
from rest_framework import serializers


class ContactoSerializer(serializers.ModelSerializer):
    def to_representation(self, instance):
        if isinstance(instance, Categoria):
            return CategoriaSerializer(instance=instance).data

    class Meta:
        model = Contacto
        fields = ['Nombre', 'Email', 'Ciudad', 'Asunto', 'Fecha_Nacimiento', 'Mensaje']


class PersonaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Persona
        fields = ['Persona_id', 'Contacto']


class ClienteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cliente
        fields = '__all__'


class ProductoSerializer(serializers.ModelSerializer):

    combos = serializers.StringRelatedField(many=True, read_only=False)

    class Meta:
        model = Producto
        fields = ['Nombre', 'Precio', 'IsBebida', 'IsPlato', 'Descripcion', 'Foto', 'Categoria','combos']


class Detalle_orden_menuSerializer(serializers.ModelSerializer):
    class Meta:
        model = Detalle_orden_menu
        fields = ['Orden_Menu', 'Producto', 'Descripcion']


class ComboSerializer(serializers.ModelSerializer):
    class Meta:
        model = Combo
        fields = '__all__'


class ComboProductoSerializer(serializers.ModelSerializer):


    class Meta:
        model = ComboProducto
        fields = ['IsCombo', 'Combo', 'Producto']


class ConsumidorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Consumidor
        fields = ['Consumidor_id']


class Orden_MenuSerializer(serializers.ModelSerializer):
    class Meta:
        model = Orden_Menu
        fields = ['Cliente', 'Fecha', 'Total']


class CategoriaSerializer(serializers.ModelSerializer):
    tracks = serializers.StringRelatedField(many=True, read_only=False)


    class Meta:
        model = Categoria
        fields = ['Nombre', 'Descripcion', 'tracks']
