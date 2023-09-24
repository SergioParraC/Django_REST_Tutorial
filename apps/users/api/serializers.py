from rest_framework import serializers
from apps.users.models import User

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'

    #Encriptar la contraseña cuando se crea un usuario nuevo
    def create(self, validate_data):
        user = User(**validate_data)
        user.set_password(validate_data['password'])
        user.save()
        return user
    
    #Encripta la contraseña cuando se modifica la información
    def update(self, instance, validate_data):
        updated_user = super().update(instance, validate_data)
        updated_user.set_password(validate_data['password'])
        updated_user.save()
        return updated_user

class UserListSerializer(serializers.ModelSerializer):
    class Meta:
        model = User

    def to_representation(self, instance):
        return {
            'id': instance['id'],
            'username': instance['username'],
            'email': instance['email'],
            'password':instance['password']
        }