from django.db import models

# Create your models here.
class Cliente(models.Model):
    id_cliente = models.AutoField(primary_key=True)
    nombre_cliente = models.CharField(max_length=35)
    correo = models.CharField(max_length=35)
    contrasenia = models.CharField(max_length=12)
    puntos = models.IntegerField(default=0, blank=True)
    class Meta:
        db_table = 'clientes' #tabla clientes que esta en base de datos cafeteria

    def __str__(self):
        return self.nombre_cliente
    

#Si necesitas hacer las migraciones agregale un default=0 a todas las columnas, ejemplo: id_cliente = models.AutoField(primary_key=True, default= 0)
#hecho eso deja el codigo tal como estaba antes ;)