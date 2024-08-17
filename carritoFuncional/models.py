# models.py
from django.db import models
from django.conf import settings
from django.dispatch import receiver
from django.db.models.signals import post_delete, post_save
import os

class Cart(models.Model):
    name = models.CharField(max_length=255)
    price = models.IntegerField()
    image = models.CharField(max_length=255, null=True, blank=True)
    quantity = models.IntegerField()

    class Meta:
        db_table = 'carrito'

    def __str__(self):
        return self.name

class Product(models.Model):
    name = models.CharField(max_length=255)
    price = models.IntegerField()
    image = models.ImageField(upload_to='products/')

    def save(self, *args, **kwargs):
        # Si el producto ya existe en la base de datos, guarda la referencia de la imagen anterior
        if self.pk:
            old_product = Product.objects.get(pk=self.pk)
            if old_product.image and old_product.image != self.image:
                old_product.image.delete(save=False)
        super(Product, self).save(*args, **kwargs)

    def delete(self, *args, **kwargs):
        # Eliminar el archivo de imagen del sistema de archivos
        self.image.delete(save=False)
        super(Product, self).delete(*args, **kwargs)

    class Meta:
        db_table = 'productos'

    def __str__(self):
        return self.name

@receiver(post_delete, sender=Product)
def auto_delete_file_on_delete(sender, instance, **kwargs):
    if instance.image:
        instance.image.delete(save=False)

@receiver(post_delete, sender=Product)
def delete_cart_items_on_product_delete(sender, instance, **kwargs):
    Cart.objects.filter(name=instance.name).delete()
