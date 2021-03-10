from rest_framework import viewsets, permissions
from rest_framework.response import Response
from users.api.serializers import ecdtUsuarioSerializer
from users.models import ecdtUsuario


class ecdtUsuarioViewSet(viewsets.ModelViewSet):
    """ Endpoint público para criar/alterar/deletar/obter usuários."""
    queryset = ecdtUsuario.objects.all()
    serializer_class = ecdtUsuarioSerializer
    permission_classes = [permissions.AllowAny]


