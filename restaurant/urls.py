from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import PlatoViewSet, PedidoViewSet

router = DefaultRouter()
router.register(r'pedidos', PedidoViewSet, basename='pedido')
router.register(r'platos', PlatoViewSet, basename='plato')

urlpatterns = [
    path('', include(router.urls)),
]