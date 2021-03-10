from django.contrib import admin
from users.models import ecdtUsuario
from projects.models import egstGerenciamento, eptfProjeto

# Register your models here.
admin.site.register(ecdtUsuario)
admin.site.register(egstGerenciamento)
admin.site.register(eptfProjeto)
