from django.http import HttpResponse
from .models import Producto,Detalle_orden_menu,Combo,ComboProducto,Consumidor,Persona,Contacto,Cliente,Categoria,Orden_Menu
from rest_framework import viewsets
from .serializers import ProductoSerializer,Detalle_orden_menuSerializer,ComboSerializer,ComboProductoSerializer,PersonaSerializer,ContactoSerializer,ConsumidorSerializer,ClienteSerializer,CategoriaSerializer,Orden_MenuSerializer


# Create your views here.

class ProductoViewSet(viewsets.ModelViewSet):   
    queryset = Producto.objects.all()
    serializer_class = ProductoSerializer


class Detalle_orden_menuViewSet(viewsets.ModelViewSet):   
    queryset = Detalle_orden_menu.objects.all()
    serializer_class = Detalle_orden_menuSerializer

class ComboViewSet(viewsets.ModelViewSet): 
    lookup_field='Descripcion'   
    queryset = Combo.objects.all()
    serializer_class = ComboSerializer


class ComboProductoViewSet(viewsets.ModelViewSet):    
    queryset = ComboProducto.objects.all()
    serializer_class = ComboProductoSerializer

class PersonaViewSet(viewsets.ModelViewSet):
    queryset = Persona.objects.all()
    serializer_class = PersonaSerializer


class ContactoViewSet(viewsets.ModelViewSet):
    queryset = Contacto.objects.all()
    serializer_class = ContactoSerializer

class ClienteViewSet(viewsets.ModelViewSet):
    queryset = Cliente.objects.all()
    serializer_class = ClienteSerializer

class ConsumidorViewSet(viewsets.ModelViewSet):
    queryset = Consumidor.objects.all()
    serializer_class = ConsumidorSerializer

class Orden_MenuViewSet(viewsets.ModelViewSet):
    queryset = Orden_Menu.objects.all()
    serializer_class = Orden_MenuSerializer

class CategoriaViewSet(viewsets.ModelViewSet):
    lookup_field='Nombre'
    queryset = Categoria.objects.all()
    serializer_class = CategoriaSerializer

