from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    #Se utiliza el include para añadir un archivo adicional del urls
    #El primer url es para hacer referencia a la app, y se pone la ruta donde estan los urls
    path('usuario/', include('apps.users.api.urls')),
    path('products/', include('apps.products.api.views.urls'))
]
