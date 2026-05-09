from rest_framework import serializers
from .models import Plato, Pedido


class PlatoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Plato
        fields = ['id', 'nombre', 'precio', 'categoria']


class PedidoSerializer(serializers.ModelSerializer):
    # Punto extra: muestra los nombres de los platos en el JSON del pedido
    nombres_platos = serializers.SerializerMethodField()

    class Meta:
        model = Pedido
        fields = ['id', 'fecha', 'total', 'estado', 'platos', 'nombres_platos']

    def get_nombres_platos(self, obj):
        return [plato.nombre for plato in obj.platos.all()]