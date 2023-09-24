from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.decorators import api_view
from apps.users.models import User
from apps.users.api.serializers import UserSerializer

#Ahora se va a utilizar un decorador en vez de una clase, en el decorador se le tiene que añadir
#Los metodos que se van a ingresar, en este caso son GET y POST
@api_view(['GET', 'POST'])
def user_api_view(request):
    #Se cambia la estructura de clase a funcion, se tiene que comporbar el tipo de metodo enviado para
    #las difetentes acciones que debe realizar

    #Cuando se hace un GET, solo imprime la información solicitada
    if request.method =='GET':
        #Extrae la información que se requiere
        users = User.objects.all()
        #Se hace el tratamiento de la información, se pone many=True porque va a traer muchos archivos
        user_serializer = UserSerializer(users, many= True)
        #Se retorna con response a la vista, PERO la informacion se encuentra en el atributo .data
        return Response(user_serializer.data)
    
    #Cuando se hace un POST, se puede usar el serializer para corroborar que la info sea correcta
    elif request.method == 'POST':
        #Se llama la informacion que viene del request
        user_serializer = UserSerializer(data = request.data)
        #Se valida la informacion si es valida
        if user_serializer.is_valid():
            #Se guarda la informacion en la base de datos
            user_serializer.save()
            return Response(user_serializer.data)
        return Response(user_serializer.errors)

#Se crea la vista de detalle de cada usuario, tambien se le agrega los metodos PUT y DELETE
@api_view(['GET', 'PUT', 'DELETE'])
def user_detail_api_view(request, pk=None):

    #A la funcion se le ingresa el pk, o el parametro de consulta, que se va desde la url
    #Se define cada uno de los metodos, en GET se muestra el detalle
    if request.method == 'GET':
        user = User.objects.filter(id = pk).first()
        user_serializer = UserSerializer(user)
        return Response(user_serializer.data)
    #Este se utiliza para acutalizar la info, comprueba por medio del serializer la info enviada
    elif request.method == 'PUT':
        user = User.objects.filter(id = pk).first()
        user_serializer = UserSerializer(user, data = request.data)
        if user_serializer.is_valid():
            user_serializer.save()
            return Response(user_serializer.data)
        return Response(user_serializer.errors)
    #Elimina la información
    elif request.method == 'DELETE':
        user = User.objects.filter(id = pk).first()
        user.delete()
        return Response('Eliminado')