# Generated by Django 5.0.6 on 2024-06-24 00:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Paginas', '0005_alter_cliente_puntos'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cliente',
            name='contrasenia',
            field=models.CharField(max_length=12),
        ),
        migrations.AlterField(
            model_name='cliente',
            name='correo',
            field=models.CharField(max_length=35),
        ),
        migrations.AlterField(
            model_name='cliente',
            name='id_cliente',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='cliente',
            name='nombre_cliente',
            field=models.CharField(max_length=35),
        ),
    ]
