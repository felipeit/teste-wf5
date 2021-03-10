from rest_framework import viewsets, permissions
from projects.models import eptfProjeto, egstGerenciamento
from projects.api.serializers import eptfProjetoSerializer, egstGerenciamentoSerializer, WorkspacesSerializer

class Workspaces(viewsets.ViewSet):
    #permission_classes = [permissions.IsAuthenticated]
    def list(self, request):
        queryset = eptfProjeto.objects.all()
        serializer = WorkspacesSerializer(queryset, many=True)
        return Response(serializer.data)

class eptfProjetoViewSet(viewsets.ModelViewSet):
    queryset = eptfProjeto.objects.all()
    serializer_class = eptfProjetoSerializer
    #permission_classes = [permissions.IsAuthenticated]

class egstGerenciamentoViewSet(viewsets.ModelViewSet):
    queryset = egstGerenciamento.objects.all()
    serializer_class = egstGerenciamentoSerializer
    #permission_classes = [permissions.IsAuthenticated]