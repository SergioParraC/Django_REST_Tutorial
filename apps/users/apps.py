from django.apps import AppConfig


class UsersConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    #Cambio de actualización, se debe especificar la carpeta donde esta la aplicacion
    name = 'apps.users'
