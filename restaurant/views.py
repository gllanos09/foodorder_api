from rest_framework import viewsets, filters
from .models import Plato, Pedido
from .serializers import PlatoSerializer, PedidoSerializer


class PlatoViewSet(viewsets.ModelViewSet):
    """
    CRUD completo para Platos.
    Búsqueda por nombre y categoría: /api/platos/?search=
    """
    queryset = Plato.objects.all()
    serializer_class = PlatoSerializer
    filter_backends = [filters.SearchFilter]
    search_fields = ['nombre', 'categoria']


class PedidoViewSet(viewsets.ModelViewSet):
    """
    CRUD completo para Pedidos.
    Búsqueda por estado: /api/pedidos/?search=
    """
    queryset = Pedido.objects.all()
    serializer_class = PedidoSerializer
    filter_backends = [filters.SearchFilter]
    search_fields = ['estado']