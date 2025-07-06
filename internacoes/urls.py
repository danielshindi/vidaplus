from rest_framework.routers import DefaultRouter
from .views import InternacaoViewSet, LeitoViewSet

router = DefaultRouter()
router.register(r'internacoes', InternacaoViewSet)
router.register(r'leitos', LeitoViewSet)

urlpatterns =router.urls