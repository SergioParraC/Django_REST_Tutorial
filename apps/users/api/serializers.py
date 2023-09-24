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
        return value
    
    def validate_email(self, value):
        if '' == value:
            raise serializers.ValidationError('Error, ingrese un correo')
        #Se puede validar de esta manera dentro de las funciones entre fields, en vez del validate general
        return value
    
    def validate(self, data):
        if data['name'] in data['email']:
            raise serializers.ValidationError('El nombre no puede estar en el email')
        return data
    
    def create(self, validated_data):
        #Para guardar la info, se puede llamar la el modelo:
        return User.objects.create(**validated_data)
        #O se puede llamar el modelo que está definido en el serializer:
        #return self.model.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.name = validated_data.get('name', instance.name)
        instance.email = validated_data.get('email', instance.email)
        #El .save() es del modelo pasado al serializer desde la vista, esto es durante el queryset
        instance.save()
        return instance

    #Este save hace parte del serializer, nada que ver con el modelo
    def save(self):
        print(self)



    
    