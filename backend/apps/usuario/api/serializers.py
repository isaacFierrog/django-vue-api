from rest_framework import serializers
from apps.usuario.models import Usuario


class UsuarioSerializer(serializers.ModelSerializer):
    class Meta:
        model = Usuario
        fields = '__all__'
        
    def create(self, validated_data):
        usuario = Usuario(**validated_data)
        usuario.set_password(validated_data['password'])
        usuario.save()
        return usuario
    
    def update(self, instance, validated_data):
        usuario = super().update(instance, validated_data)
        usuario.set_password(validated_data['password'])
        usuario.save()
        return usuario
    
    
class UsuarioTokenSerializer(serializers.ModelSerializer):
    class Meta:
        model = Usuario
        fields = (
            'correo',
            'nombre',
            'apellido'
        )