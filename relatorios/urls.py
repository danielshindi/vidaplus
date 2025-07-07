from rest_framework.routers import DefaultRouter
from .views import RelatorioViewSet

router = DefaultRouter()
router.register(r'', RelatorioViewSet)

urlpatterns = router.urls