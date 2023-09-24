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
    if request.method =='GET':
        #Extrae la información que se requiere
        users = User.objects.all()
        #Se hace el tratamiento de la información, se pone many=True porque va a traer muchos archivos
        user_serializer = UserSerializer(users, many= True)
        #Se retorna con response a la vista, PERO la informacion se encuentra en el atributo .data
        return Response(user_serializer.data)
    elif request.method == 'POST':
        print(request.data)