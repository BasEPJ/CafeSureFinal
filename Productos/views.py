from django.shortcuts import render, redirect
from .models import Productos
from django.contrib import messages




# Create your views here.


def ProductosPag(request):
    productosListados = Productos.objects.all()
    messages.success(request, '¡Productos listados!')
    return render(request, "gestionProductos.html", {"productos": productosListados})


def registrarProductos(request):
    codigo = request.POST['txtCodigo']
    nombre = request.POST['txtNombre']
    creditos = request.POST['numCreditos']

    productos = Productos.objects.create(
        codigo=codigo, nombre=nombre, creditos=creditos)
    messages.success(request, '¡Producto registrado!')
    return redirect('ProductosPag')


def edicionProductos(request, codigo):
    productos = Productos.objects.get(codigo=codigo)
    return render(request, "edicionProductos.html", {"producto": productos})


def filtrarProductos(request):
    if request.method == 'POST':
        codigo = request.POST.get('codigo')
        if codigo:
            productosFiltrados = Productos.objects.filter(codigo__icontains=codigo)
        else:
            productosFiltrados = Productos.objects.all()
        return render(request, "gestionProductos.html", {"productos": productosFiltrados})
    else:
        return redirect('ProductosPag')


def editarProductos(request):
    if request.method == 'POST':
        codigo = request.POST['codigo']
        nombre = request.POST['nombre']
        creditos = request.POST['creditos']

        productos = Productos.objects.get(codigo=codigo)
        productos.nombre = nombre
        productos.creditos = creditos
        productos.save()

        messages.success(request, '¡Producto actualizado!')

        return redirect('ProductosPag')
    else:
        messages.error(request, 'Error al actualizar el producto.')
        return redirect('ProductosPag')


def eliminarProductos(request, codigo):
    productos = Productos.objects.get(codigo=codigo)
    productos.delete()
    messages.success(request, '¡Producto eliminado!')
    return redirect('ProductosPag')


