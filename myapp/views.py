from django.http import HttpResponse
from .models import *
from rest_framework import viewsets
from .serializers import *

def index(request):
    return HttpResponse("Hello, estamos empezando Café Real")
# Create your views here.

class ProductoViewSet(viewsets.ModelViewSet):   
    queryset = Producto.objects.all()
    serializer_class = ProductoSerializer


class Detalle_orden_menuViewSet(viewsets.ModelViewSet):   
    queryset = Detalle_orden_menu.objects.all()
    serializer_class = Detalle_orden_menuSerializer

class ComboViewSet(viewsets.ModelViewSet):   
    queryset = Combo.objects.all()
    serializer_class = ComboSerializer


class ComboProductoViewSet(viewsets.ModelViewSet):    
    queryset = ComboProducto.objects.all()
    serializer_class = ComboProductoSerializer