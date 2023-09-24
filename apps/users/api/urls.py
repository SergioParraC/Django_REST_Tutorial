from django.urls import path
from apps.users.api.api import UserAPIView

urlpatterns = [
    #Se crea el nuevo enlace, se llama a la vista
    path('usuario/', UserAPIView.as_view(), name = 'usuario_api')
]
