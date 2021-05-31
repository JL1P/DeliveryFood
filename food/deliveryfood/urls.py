from django.urls import path, include
from rest_framework.routers import DefaultRouter
from . import views

router = DefaultRouter()

router.register('imagenes_sitio', views.ImagenesSitioViewSet, basename='imagenes_sitio')
router.register('pedido', views.PedidoViewSet, basename='pedidos')
router.register('mensajero', views.MensajeroViewSet, basename='mensajeros')
router.register('producto', views.ProductoViewSet, basename='productos')
router.register('categoria', views.CategoriaViewSet, basename='categorias')
router.register('administrador', views.AdministradorViewSet, basename='administradores')
router.register('usuario', views.UsuarioViewSet, basename='usuarios')
router.register('restaurante', views.RestauranteViewSet, basename='restaurantes')
router.register('reporte_all', views.ReporteAllViewSet, basename='reporte_alls')
router.register('reporte', views.ReporteViewSet, basename='reportes')
router.register('valoracion', views.ValoracionViewSet, basename='valoraciones')

urlpatterns = [
    path('', include(router.urls))
]