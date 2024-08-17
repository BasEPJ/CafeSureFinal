from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('',views.inicio,name='inicio' ),
    path('menu',views.menu,name='menu' ),
    path('contactanos',views.contactanos,name='contactanos' ),
    path('canjeoPuntos',views.canjeoPuntos,name='canjeoPuntos' ),
    path('ubicacion',views.ubicacion,name='ubicacion' ),
    path('carrito',views.carrito,name='carrito' ),
    path('fotos',views.fotos,name='fotos' ),

    path('productos',views.productos,name='productos' ),

    #Todo el CRUD de clientes
    path('crearCliente',views.crearCliente,name='crearCliente' ),
    path('listarCliente',views.listarCliente,name='listarCliente' ),
    path('filtrarCliente',views.filtrarCliente,name='filtrarCliente' ),
    path('modificarCliente/<id_cliente>/',views.modificarCliente,name='modificarCliente' ),
    path('eliminarCliente/<id_cliente>/',views.eliminarCliente,name='eliminarCliente' ),

    #Inicio y cierre de sesion del cliente
    path('sesionCliente',views.sesionCliente,name='sesionCliente'),
    path('cerrarSesionCliente',views.cerrarSesionCliente,name='cerrarSesionCliente'),


    path('home', views.home,name='home'),


]
