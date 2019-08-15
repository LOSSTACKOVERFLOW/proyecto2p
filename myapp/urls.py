from django.urls import path
from . import views
from  rest_framework import routers 

router = routers.DefaultRouter()
router.register(r'Contacto', views.ContactoViewSet)
router.register(r'Persona', views.PersonaViewSet)
router.register(r'Cliente', views.ClienteViewSet)
router.register(r'Consumidor', views.ConsumidorViewSet)
router.register(r'Orden_Menu', views.Orden_MenuViewSet)
router.register(r'Categoria', views.CategoriaViewSet)
router.register(r'Producto', views.ProductoViewSet)
router.register(r'Detalle_orden_menu', views.Detalle_orden_menuViewSet)
router.register(r'Combo', views.ComboViewSet)
router.register(r'ComboProducto', views.ComboProductoViewSet)
urlpatterns = [
   
]
urlpatterns+=router.urls