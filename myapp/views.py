from django.http import HttpResponse
from django.contrib.auth.models import *
from rest_framework import viewsets
from proyecto2p.myapp.serializers import *

def index(request):
    return HttpResponse("Hello, estamos empezando Café Real")
# Create your views here.

class PersonaViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = Persona.objects.all()
    serializer_class = PersonaSerializer


class ContactoViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = Contacto.objects.all()
    serializer_class = ContactoSerializer

class ClienteViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = Cliente.objects.all()
    serializer_class = ClienteSerializer

class ConsumidorViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = Consumidor.objects.all()
    serializer_class = ConsumidorSerializer

class Orden_MenuViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = Orden_Menu.objects.all()
    serializer_class = Orden_MenuSerializer

class CategoriaViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = Categoria.objects.all()
    serializer_class = CategoriaSerializer

class ProductoViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = Producto.objects.all()
    serializer_class = ProductoSerializer

class Detalle_orden_menuViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = Detalle_orden_menu.objects.all()
    serializer_class = Detalle_orden_menuSerializer


class ComboViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = Combo.objects.all()
    serializer_class = ComboSerializer

class ComboProductoViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = ComboProducto.objects.all()
    serializer_class = ComboProductoSerializer

