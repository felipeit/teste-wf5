from rest_framework import viewsets
from rest_framework.response import Response
from users.api.serializers import ecdtUsuarioSerializer
from users.models import ecdtUsuario


class ecdtUsuarioViewSet(viewsets.ModelViewSet):
    queryset = ecdtUsuario.objects.all()
    serializer_class = ecdtUsuarioSerializer
