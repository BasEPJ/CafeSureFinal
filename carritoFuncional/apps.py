from django.apps import AppConfig

class CarritoFuncionalConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'carritoFuncional'

    def ready(self):
        import carritoFuncional.signals  # Asegúrate de importar las señales 