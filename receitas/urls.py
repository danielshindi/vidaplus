from rest_framework.routers import DefaultRouter
from .views import ReceitaViewSet

router = DefaultRouter()
router.register(r'receitas', ReceitaViewSet)

urlpatterns = router.urls
