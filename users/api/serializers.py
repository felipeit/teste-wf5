from rest_framework import serializers
from users.models import ecdtUsuario


class ecdtUsuarioSerializer(serializers.ModelSerializer):
    password = serializers.CharField(required=True)
    class Meta:
        model = ecdtUsuario
        fields = [
            'idUsuario', 
            'nmUsuario', 
            'nmEmail',
            'nmPerfil',
            'password'
            ]
    #def get_passowrd(self, obj):        
    def create(self, validated_data):
        user = ecdtUsuario(**validated_data)
        password = validated_data.pop('password', None)
        user.set_password(password)
        user.save()
        return user

