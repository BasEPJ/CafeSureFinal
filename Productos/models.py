from django.db import models

class Productos(models.Model):
    codigo = models.CharField(primary_key=True, max_length=6)
    nombre = models.CharField(max_length=50)
    creditos = models.PositiveSmallIntegerField()

    class Meta:
        db_table = 'productos_productos'  # Especifica el nombre correcto de la tabla en la base de datos

    def __str__(self):
        texto = "{0} ({1})"
        return texto.format(self.nombre, self.creditos)
