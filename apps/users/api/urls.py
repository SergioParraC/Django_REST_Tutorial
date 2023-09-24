from django.urls import path
from apps.users.api.api import user_api_view

urlpatterns = [
    #Se crea el nuevo enlace, se llama a la vista
    path('usuario/', user_api_view, name = 'usuario_api')
]
