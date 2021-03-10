from rest_framework import serializers
from projects.models import eptfProjeto, egstGerenciamento


class eptfProjetoSerializer(serializers.ModelSerializer):
    class Meta:
        model = eptfProjeto
        fields = '__all__'


class egstGerenciamentoSerializer(serializers.ModelSerializer):
    class Meta:
        model = egstGerenciamento
        fields = '__all__'
