# signals.py
from django.db.models.signals import post_delete
from django.dispatch import receiver
from .models import Product, Cart

@receiver(post_delete, sender=Product)
def delete_cart_items_on_product_delete(sender, instance, **kwargs):
    Cart.objects.filter(name=instance.name).delete()

@receiver(post_delete, sender=Product)
def auto_delete_file_on_delete(sender, instance, **kwargs):
    if instance.image:
        instance.image.delete(save=False)