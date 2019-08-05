from .models import *
from rest_framework import serializers

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