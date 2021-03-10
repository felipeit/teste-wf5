from rest_framework import routers
from projects.api import views


router = routers.DefaultRouter()

router.register(r'projetos', views.eptfProjetoViewSet)
router.register(r'gerenciamento', views.egstGerenciamentoViewSet)