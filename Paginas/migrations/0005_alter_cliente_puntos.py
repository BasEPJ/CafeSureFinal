# Generated by Django 5.0.6 on 2024-06-23 04:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Paginas', '0004_remove_cliente_id_remove_cliente_nombre_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cliente',
            name='puntos',
            field=models.IntegerField(blank=True, default=0),
        ),
    ]
