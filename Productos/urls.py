from django.urls import path
from . import views

urlpatterns = [
    path('ProductosPag/', views.ProductosPag, name='ProductosPag'),
    path('filtrarProductos/', views.filtrarProductos, name='filtrarProductos'),
    path('registrarProductos/', views.registrarProductos, name='registrarProductos'),
    path('edicionProductos/<codigo>/', views.edicionProductos, name='edicionProductos'),
    path('editarProductos/', views.editarProductos, name='editarProductos'),
    path('eliminarProductos/<codigo>/', views.eliminarProductos, name='eliminarProductos'),
]