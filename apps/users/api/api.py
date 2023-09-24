from rest_framework.views import APIView
from rest_framework.response import Response
from apps.users.models import User
from apps.users.api.serializers import UserSerializer

class UserAPIView(APIView):

    def get(self, request):
        #Extrae la información que se requiere
        users = User.objects.all()
        #Se hace el tratamiento de la información, se pone many=True porque va a traer muchos archivos
        user_serializer = UserSerializer(users, many= True)
        #Se retorna con response a la vista, PERO la informacion se encuentra en el atributo .data
        return Response(user_serializer.data)