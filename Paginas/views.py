from django.shortcuts import render, get_object_or_404, redirect
from django.contrib import messages
from .forms import ClienteForm
from .forms import ModificarClienteForm
from .models import Cliente

# Create your views here.
def home(request):
    return render(request, 'home.html')

def inicio(request):
    if 'cliente' in request.session:
        id_cliente = request.session['cliente']
        try:
            cliente = Cliente.objects.get(id_cliente=id_cliente)
            return render(request, 'inicio.html', {'nombre_cliente': cliente.nombre_cliente})
        except Cliente.DoesNotExist:
            # Manejar el caso en que el cliente no existe
            pass
    
    # Si no hay sesion de cliente o el cliente no existe
    return render(request, 'inicio.html')

def menu(request):
    return render(request, 'menu.html')

def contactanos(request):
    return render(request, 'contactanos.html')

def canjeoPuntos(request):
    return render(request, 'canjeoPuntos.html')

def ubicacion(request):
    return render(request, 'ubicacion.html')

def carrito(request):
    return render(request, 'carrito.html')

def productos(request):
    return render(request, 'productos.html')

def fotos(request):
    return render(request, 'fotos.html')


#Todo el CRUD del cliente

def crearCliente(request):
    if request.method == 'POST':
        form = ClienteForm(request.POST)
        if form.is_valid():
            cliente = form.save()
            return render(request, 'inicio.html', {'cliente': cliente})
        else:
            messages.error(request, 'Por favor, corrija los errores a continuación.')
    else:
        form = ClienteForm()
    return render(request, 'crearCliente.html', {'form': form})

def listarCliente(request):
    clientes = Cliente.objects.all()
    return render(request, 'listarCliente.html', {'clientes': clientes})

def modificarCliente(request, id_cliente):
    cliente = Cliente.objects.get(id_cliente=id_cliente)
    
    if request.method == 'POST':
        form = ModificarClienteForm(request.POST, instance=cliente)
        if form.is_valid():
            form.save()
            return redirect('listarCliente')  
    else:
        form = ModificarClienteForm(instance=cliente)
    
    return render(request, 'modificarCliente.html', {'form': form, 'cliente': cliente})

def filtrarCliente(request):
    clientes = Cliente.objects.filter(nombre_cliente=request.POST["nombre_cliente"])
    return render(request, 'listarCliente.html', {'clientes': clientes})


def eliminarCliente(request, id_cliente):
    cliente = Cliente.objects.get(id_cliente=id_cliente)
    cliente.delete()
    return redirect('listarCliente')


#Inicio y cierre de sesion del cliente

def sesionCliente(request):
    if request.method == 'POST':
        correo = request.POST.get('correo')
        contrasenia = request.POST.get('contrasenia')
        
        if correo and contrasenia:
            try:
                clienteLog = Cliente.objects.get(correo=correo, contrasenia=contrasenia)
                request.session['cliente'] = clienteLog.id_cliente
                return redirect('inicio')  
            except Cliente.DoesNotExist:
                messages.error(request, 'Correo o contraseña incorrectos')
        else:
            messages.error(request, 'Por favor, ingrese correo y contraseña')
    
    return render(request, 'sesionCliente.html')

def cerrarSesionCliente(request):
    if 'cliente' in request.session:
        del request.session['cliente']
    messages.success(request, 'Has cerrado sesión exitosamente.')
    return redirect('inicio')






