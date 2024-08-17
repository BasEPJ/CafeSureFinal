from django.shortcuts import render, redirect, get_object_or_404
from django.core.files.storage import FileSystemStorage
from .models import Product, Cart
from django.contrib import messages

def index(request):
    display_message = None
    if request.method == 'POST':
        product_name = request.POST['product_name']
        product_price = request.POST['product_price']
        product_image = request.FILES['product_image']
        
        fs = FileSystemStorage()
        product_image_name = fs.save(product_image.name, product_image)
        
        product = Product(name=product_name, price=product_price, image=product_image_name)
        product.save()
        display_message = "Producto añadido exitosamente"
    
    cart_count = Cart.objects.count()
    
    return render(request, 'carritoFuncional/index.html', {
        'display_message': display_message,
        'cart_count': cart_count
    })

def shop_product(request):
    display_messages = []

    if request.method == 'POST':
        product_name = request.POST['product_name']
        product_price = request.POST['product_price']
        product_image = request.POST['product_image']
        product_quantity = 1

        cart_item = Cart.objects.filter(name=product_name).first()

        if cart_item:
            display_messages.append('El Producto ya ha sido añadido al carrito')
        else:
            Cart.objects.create(name=product_name, price=product_price, image=product_image, quantity=product_quantity)
            display_messages.append('El Producto fue añadido correctamente')

    products = Product.objects.all()
    cart_count = Cart.objects.count()

    return render(request, 'carritoFuncional/shop_product.html', {
        'products': products,
        'display_messages': display_messages,
        'cart_count': cart_count
    })

from django.conf import settings
from django.shortcuts import render, redirect
from .models import Cart

def cart(request):
    if request.method == 'POST':
        if 'update_cart_quantity' in request.POST:
            update_id = request.POST['update_quantity_id']
            update_value = request.POST['update_quantity']
            Cart.objects.filter(id=update_id).update(quantity=update_value)
            return redirect('cart')

    if request.GET.get('remove'):
        remove_id = request.GET.get('remove')
        Cart.objects.filter(id=remove_id).delete()
        messages.success(request, 'Objeto removido del carrito')
        return redirect('cart')

    if request.GET.get('delete_all'):
        Cart.objects.all().delete()
        messages.success(request, 'Todos los Objetos removidos del carrito')
        return redirect('cart')

    cart_items = Cart.objects.all()
    grand_total = sum(item.price * item.quantity for item in cart_items)
    cart_count = Cart.objects.count()

    return render(request, 'carritoFuncional/cart.html', {
        'cart_items': cart_items,
        'grand_total': grand_total,
        'cart_count': cart_count,
        'MEDIA_URL': settings.MEDIA_URL  # Añadir MEDIA_URL al contexto
    })


def view_products(request):
    query = request.GET.get('q', '')
    if query:
        products = Product.objects.filter(name__icontains=query)
    else:
        products = Product.objects.all()

    return render(request, 'carritoFuncional/view_products.html', {
        'products': products,
        'query': query,
    })

def delete_product(request, product_id):
    product = get_object_or_404(Product, id=product_id)
    product.delete()
    messages.success(request, 'Producto removido exitosamente')
    return redirect('view_products')

def update_product(request, product_id):
    product = get_object_or_404(Product, id=product_id)
    if request.method == 'POST':
        product.name = request.POST.get('update_product_name')
        product.price = request.POST.get('update_product_price')
        
        # Manejar la actualización de la imagen
        if 'update_product_image' in request.FILES:
            product.image = request.FILES['update_product_image']
        
        product.save()

        # Actualizar la referencia de imagen en los elementos del carrito
        Cart.objects.filter(name=product.name).update(image=product.image.name)
        
        messages.success(request, 'Producto actualizado exitosamente')
        return redirect('view_products')
    
    return render(request, 'carritoFuncional/update_product.html', {'product': product})