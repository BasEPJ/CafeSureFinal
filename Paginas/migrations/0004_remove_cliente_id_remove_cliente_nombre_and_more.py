# Generated by Django 5.0.6 on 2024-06-23 03:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Paginas', '0003_auto_20240621_1932'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='cliente',
            name='id',
        ),
        migrations.RemoveField(
            model_name='cliente',
            name='nombre',
        ),
        migrations.AddField(
            model_name='cliente',
            name='id_cliente',
            field=models.AutoField(default=0, primary_key=True, serialize=False),
        ),
        migrations.AddField(
            model_name='cliente',
            name='nombre_cliente',
            field=models.CharField(default=0, max_length=35),
        ),
        migrations.AddField(
            model_name='cliente',
            name='puntos',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='cliente',
            name='contrasenia',
            field=models.CharField(default=0, max_length=12),
        ),
        migrations.AlterField(
            model_name='cliente',
            name='correo',
            field=models.CharField(default=0, max_length=35),
        ),
        migrations.AlterModelTable(
            name='cliente',
            table='clientes',
        ),
    ]
