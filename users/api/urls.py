from rest_framework import routers
from users.api import views
from users.models import ecdtUsuario

router = routers.DefaultRouter()
router.register('cadastrar', views.ecdtUsuarioViewSet, basename='ecdtUsuario')