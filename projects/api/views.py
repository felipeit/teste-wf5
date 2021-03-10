from rest_framework import viewsets, permissions
from projects.models import eptfProjeto, egstGerenciamento
from projects.api.serializers import eptfProjetoSerializer, egstGerenciamentoSerializer, WorkspacesSerializer


class eptfProjetoViewSet(viewsets.ModelViewSet):
    """ Endpoint privado para criar/alterar/deletar/obter prjetos."""
    queryset = eptfProjeto.objects.all()
    serializer_class = eptfProjetoSerializer
    permission_classes = [permissions.IsAuthenticated]

class egstGerenciamentoViewSet(viewsets.ModelViewSet):
    """ Endpoint privado para criar/alterar/deletar/obter gerenciamento do projeto."""
    queryset = egstGerenciamento.objects.all()
    serializer_class = egstGerenciamentoSerializer
    permission_classes = [permissions.IsAuthenticated]