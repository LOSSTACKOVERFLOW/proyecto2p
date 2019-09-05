from django.shortcuts import render
from .serializers import HistorialSerializer
from rest_framework import viewsets as meviewsets
from .models import historial
from django.http import HttpResponse


#def index(request):
 #   return HttpResponse("Hello, world. You're at the polls index.")

class HistorialViewSet(meviewsets.ModelViewSet):
    lookup_field = 'id'
    queryset = historial.objects.all()
    serializer_class = HistorialSerializer