from django.db import models
from users.models import ecdtUsuario
from datetime import datetime

class egstGerenciamento(models.Model):
    idGerenciamento = models.CharField(max_length=7, primary_key=True)
    nuProjeto = models.ForeignKey('eptfProjeto', null=False, blank=False, on_delete=models.DO_NOTHING)
    vlOrcamento = models.DecimalField(decimal_places=2, max_digits=9)
    vlGasto = models.DecimalField(decimal_places=2, max_digits=9)
    
    def __str__(self):
        return self.idGerenciamento

class eptfProjeto(models.Model):
    STATUS = [
        (1, 'Novo'),
        (2, 'Aprovado'),
        (3, 'Cancelado')  
    ]

    idProjeto = models.CharField(max_length=7, primary_key=True)
    cdProjeto = models.CharField(max_length=20)
    nmProjeto = models.CharField(max_length=80)
    deProjeto = models.CharField(max_length=2000, null=True, blank=True)
    dtCadastro = models.DateTimeField(auto_now=datetime.now())
    nuUsuario = models.ForeignKey(
        ecdtUsuario, 
        null=False, 
        blank=False, 
        on_delete=models.DO_NOTHING
        )
    dtAprovacao = models.DateField(null=True, blank=True)
    dtCancelamento = models.DateField(null=True, blank=True)
    flStatus = models.IntegerField(choices=STATUS)
    
    def __str__(self):
        return self.idProjeto