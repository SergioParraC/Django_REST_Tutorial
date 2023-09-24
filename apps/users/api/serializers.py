from rest_framework import serializers
from apps.users.models import User

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'
        
class TestUserSerializer(serializers.Serializer):
    name = serializers.CharField(max_length = 200)
    email = serializers.EmailField()

    def validate_name(self, value):
        if 'Bernabe' in value:
            raise serializers.ValidationError('Error, nadie se puede llamar Bernabe')
        print(self.context)
        return value
    
    def validate_email(self, value):
        if '' == value:
            raise serializers.ValidationError('Error, ingrese un correo')
        #Se puede validar de esta manera dentro de las funciones entre fields, en vez del validate general
        if self.validate_name(self.context['name']) in value:
            raise serializers.ValidationError('Error, el email no puede contener el nombre')
        return value
    
    def validate(self, data):
        if data['name'] in data['email']:
            raise serializers.ValidationError('El nombre no puede estar en el email')
        return data