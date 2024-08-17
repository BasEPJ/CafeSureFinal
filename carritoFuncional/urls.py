
from django.urls import path
from . import views

urlpatterns = [
    path('index/', views.index, name='index'),
    path('view_products/', views.view_products, name='view_products'),
    path('shop_product/', views.shop_product, name='shop_product'),
    path('cart/', views.cart, name='cart'),
    path('delete_product/<int:product_id>/', views.delete_product, name='delete_product'),
    path('update_product/<int:product_id>/', views.update_product, name='update_product'),
]