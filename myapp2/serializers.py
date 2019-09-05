from rest_framework import serializers
from .models import historial

class HistorialSerializer(serializers.ModelSerializer):
    class Meta:
        model= historial
        fields='__all__'
