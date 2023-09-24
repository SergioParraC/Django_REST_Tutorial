from django.contrib import admin
#Importa el modelo usuario y lo registra
from apps.users.models import User

admin.site.register(User)