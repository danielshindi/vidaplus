from rest_framework.routers import DefaultRouter
from .views import RelatorioViewSet

router = DefaultRouter()
router.register(r'relatorios', RelatorioViewSet)

urlpatterns = router.urls