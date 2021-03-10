from rest_framework import serializers
from users.models import ecdtUsuario


class ecdtUsuarioSerializer(serializers.ModelSerializer):
    class Meta:
        model = ecdtUsuario
        fields = [
            'idUsuario', 
            'nmUsuario', 
            'nmEmail',
            'nmPerfil',
            ]
            
